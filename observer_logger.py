"""
Observer Logger - Tracks observer interactions and synchronization status
Implements logging for RFT observer-based analysis and debugging
"""

import logging
import json
import time
import os
import math
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from collections import defaultdict, deque
import threading

logger = logging.getLogger(__name__)

class ObserverLogger:
    """
    Logs and tracks observer interactions for RFT analysis
    Maintains observer synchronization status and interaction history
    """
    
    def __init__(self, max_history_per_observer: int = 100):
        """Initialize observer logger with tracking capabilities"""
        
        self.max_history_per_observer = max_history_per_observer
        
        # Observer interaction tracking
        self.observer_interactions = defaultdict(lambda: deque(maxlen=max_history_per_observer))
        self.observer_metadata = defaultdict(dict)
        self.sync_status_cache = {}
        
        # Session tracking
        self.active_sessions = {}
        self.session_history = deque(maxlen=1000)
        
        # Performance metrics
        self.performance_metrics = {
            'total_interactions': 0,
            'successful_challenges': 0,
            'failed_challenges': 0,
            'average_processing_time': 0.0,
            'observer_count': 0
        }
        
        # Synchronization tracking
        self.sync_events = deque(maxlen=500)
        self.coherence_timeline = deque(maxlen=200)
        
        # Thread safety
        self.lock = threading.Lock()
        
        # Cache settings
        self.cache_timeout = 300  # 5 minutes
        
        # Observer state tracking for phase calculations
        self.observer_last_challenge = {}
        
        # Ensure logs directory exists
        os.makedirs('logs', exist_ok=True)
        
        logger.info("Observer Logger initialized with interaction tracking")
    
    def log_interaction(self, user_id: int, interaction_type: str, data: Any):
        """
        Log an observer interaction
        
        Args:
            user_id: Observer identifier
            interaction_type: Type of interaction (start, challenge_start, etc.)
            data: Interaction data (challenge text, parameters, etc.)
        """
        
        with self.lock:
            timestamp = time.time()
            
            # Create interaction record
            interaction_record = {
                'timestamp': timestamp,
                'datetime': datetime.fromtimestamp(timestamp).isoformat(),
                'user_id': user_id,
                'type': interaction_type,
                'data': data,
                'session_id': self._get_current_session_id(user_id)
            }
            
            # Add to observer history
            self.observer_interactions[user_id].append(interaction_record)
            
            # Update observer metadata
            self._update_observer_metadata(user_id, interaction_record)
            
            # Update performance metrics
            self._update_performance_metrics(interaction_type)
            
            # Log to file if enabled
            self._write_to_log_file(interaction_record)
            
            # Log observer state for challenges
            if interaction_type == 'challenge_start':
                self.log_observer_state(user_id, data)
            
            logger.debug(f"Logged interaction: {interaction_type} for observer {user_id}")
    
    def _get_current_session_id(self, user_id: int) -> Optional[str]:
        """Get current session ID for observer"""
        
        for session_id, session_data in self.active_sessions.items():
            if session_data.get('user_id') == user_id:
                return session_id
        
        return None
    
    def _update_observer_metadata(self, user_id: int, interaction_record: Dict[str, Any]):
        """Update observer metadata based on interaction"""
        
        if user_id not in self.observer_metadata:
            self.observer_metadata[user_id] = {
                'first_interaction': interaction_record['timestamp'],
                'total_interactions': 0,
                'interaction_types': defaultdict(int),
                'last_activity': interaction_record['timestamp'],
                'challenge_count': 0,
                'success_rate': 0.0,
                'average_complexity': 0.0,
                'synchronization_events': []
            }
        
        metadata = self.observer_metadata[user_id]
        metadata['total_interactions'] += 1
        metadata['interaction_types'][interaction_record['type']] += 1
        metadata['last_activity'] = interaction_record['timestamp']
        
        # Track challenge-specific metrics
        if interaction_record['type'] == 'challenge_start':
            metadata['challenge_count'] += 1
        elif interaction_record['type'] == 'challenge_complete':
            # Update success rate and complexity
            self._update_challenge_metrics(user_id, interaction_record)
    
    def _update_challenge_metrics(self, user_id: int, interaction_record: Dict[str, Any]):
        """Update challenge-specific metrics for observer"""
        
        metadata = self.observer_metadata[user_id]
        
        # Calculate success rate
        successful_challenges = metadata['interaction_types']['challenge_complete']
        total_challenges = metadata['challenge_count']
        
        if total_challenges > 0:
            metadata['success_rate'] = successful_challenges / total_challenges
        
        # Update average complexity if available
        if 'data' in interaction_record and isinstance(interaction_record['data'], dict):
            rft_params = interaction_record['data'].get('rft_params', {})
            if 'chi_liam' in rft_params:
                # Use coherence coefficient as complexity proxy
                current_complexity = rft_params['chi_liam'] / 2.718  # Normalize by base
                
                # Running average calculation
                if metadata['average_complexity'] == 0.0:
                    metadata['average_complexity'] = current_complexity
                else:
                    metadata['average_complexity'] = (metadata['average_complexity'] * 0.9 + 
                                                    current_complexity * 0.1)
    
    def _update_performance_metrics(self, interaction_type: str):
        """Update global performance metrics"""
        
        self.performance_metrics['total_interactions'] += 1
        
        if interaction_type == 'challenge_complete':
            self.performance_metrics['successful_challenges'] += 1
        elif interaction_type == 'challenge_error':
            self.performance_metrics['failed_challenges'] += 1
        
        # Update observer count
        self.performance_metrics['observer_count'] = len(self.observer_metadata)
    
    def _write_to_log_file(self, interaction_record: Dict[str, Any]):
        """Write interaction record to log file"""
        
        try:
            # Format record for logging
            log_entry = {
                'timestamp': interaction_record['timestamp'],
                'datetime': interaction_record['datetime'],
                'observer_id': interaction_record['user_id'],
                'interaction_type': interaction_record['type'],
                'data_summary': self._summarize_data(interaction_record['data'])
            }
            
            # Log as structured JSON
            logger.info(f"OBSERVER_INTERACTION: {json.dumps(log_entry)}")
            
        except Exception as e:
            logger.error(f"Failed to write interaction to log: {str(e)}")
    
    def _summarize_data(self, data: Any) -> Dict[str, Any]:
        """Create summary of interaction data for logging"""
        
        if isinstance(data, str):
            return {
                'type': 'text',
                'length': len(data),
                'preview': data[:50] + '...' if len(data) > 50 else data
            }
        elif isinstance(data, dict):
            summary = {'type': 'dict', 'keys': list(data.keys())}
            
            # Add specific summaries for known data types
            if 'rft_params' in data:
                summary['has_rft_params'] = True
            if 'challenge' in data:
                summary['challenge_length'] = len(str(data['challenge']))
            if 'processing_time' in data:
                summary['processing_time'] = data['processing_time']
            
            return summary
        else:
            return {'type': type(data).__name__, 'value': str(data)[:100]}
    
    def get_sync_status(self, user_id: int) -> str:
        """
        Get synchronization status for observer
        
        Args:
            user_id: Observer identifier
            
        Returns:
            Synchronization status string
        """
        
        # Check cache first
        cache_key = f"sync_{user_id}"
        if cache_key in self.sync_status_cache:
            cache_entry = self.sync_status_cache[cache_key]
            if time.time() - cache_entry['timestamp'] < self.cache_timeout:
                return cache_entry['status']
        
        # Calculate synchronization status
        sync_status = self._calculate_sync_status(user_id)
        
        # Cache result
        self.sync_status_cache[cache_key] = {
            'status': sync_status,
            'timestamp': time.time()
        }
        
        return sync_status
    
    def _calculate_sync_status(self, user_id: int) -> str:
        """Calculate observer synchronization status"""
        
        if user_id not in self.observer_metadata:
            return "INITIALIZING"
        
        metadata = self.observer_metadata[user_id]
        
        # Get recent interactions
        recent_interactions = list(self.observer_interactions[user_id])
        if not recent_interactions:
            return "INACTIVE"
        
        # Check recent activity (last 30 minutes)
        current_time = time.time()
        recent_cutoff = current_time - 1800  # 30 minutes
        
        recent_activity = [i for i in recent_interactions 
                          if i['timestamp'] > recent_cutoff]
        
        if not recent_activity:
            return "DORMANT"
        
        # Analyze synchronization based on success rate and activity
        success_rate = metadata['success_rate']
        total_interactions = metadata['total_interactions']
        
        if success_rate >= 0.8 and total_interactions >= 5:
            return "SYNCHRONIZED"
        elif success_rate >= 0.6 and total_interactions >= 3:
            return "ALIGNING"
        elif success_rate >= 0.4 or total_interactions >= 10:
            return "STABILIZING"
        elif total_interactions >= 1:
            return "CALIBRATING"
        else:
            return "INITIALIZING"
    
    def log_synchronization_event(self, user_id: int, event_type: str, 
                                  sync_data: Dict[str, Any]):
        """Log a synchronization event"""
        
        with self.lock:
            sync_event = {
                'timestamp': time.time(),
                'datetime': datetime.now().isoformat(),
                'observer_id': user_id,
                'event_type': event_type,
                'sync_data': sync_data
            }
            
            self.sync_events.append(sync_event)
            
            # Add to observer metadata
            if user_id in self.observer_metadata:
                self.observer_metadata[user_id]['synchronization_events'].append(sync_event)
                
                # Keep only recent sync events per observer
                events = self.observer_metadata[user_id]['synchronization_events']
                if len(events) > 20:
                    self.observer_metadata[user_id]['synchronization_events'] = events[-20:]
            
            logger.debug(f"Logged sync event: {event_type} for observer {user_id}")
    
    def log_coherence_measurement(self, coherence_value: float, 
                                  system_state: Dict[str, Any]):
        """Log system coherence measurement"""
        
        with self.lock:
            coherence_record = {
                'timestamp': time.time(),
                'datetime': datetime.now().isoformat(),
                'coherence_value': coherence_value,
                'system_state': system_state,
                'active_observers': len(self.observer_metadata)
            }
            
            self.coherence_timeline.append(coherence_record)
            
            logger.debug(f"Logged coherence measurement: {coherence_value:.4f}")
    
    def get_observer_history(self, user_id: int, limit: int = 50) -> List[Dict[str, Any]]:
        """Get interaction history for specific observer"""
        
        if user_id not in self.observer_interactions:
            return []
        
        interactions = list(self.observer_interactions[user_id])
        return interactions[-limit:] if limit else interactions
    
    def get_observer_statistics(self, user_id: int) -> Dict[str, Any]:
        """Get comprehensive statistics for observer"""
        
        if user_id not in self.observer_metadata:
            return {'error': 'Observer not found'}
        
        metadata = self.observer_metadata[user_id]
        recent_interactions = self.get_observer_history(user_id, 10)
        
        # Calculate time-based metrics
        if recent_interactions:
            first_interaction = metadata['first_interaction']
            last_interaction = metadata['last_activity']
            total_duration = last_interaction - first_interaction
            
            activity_span = timedelta(seconds=total_duration)
        else:
            activity_span = timedelta(0)
        
        statistics = {
            'observer_id': user_id,
            'sync_status': self.get_sync_status(user_id),
            'total_interactions': metadata['total_interactions'],
            'challenge_count': metadata['challenge_count'],
            'success_rate': metadata['success_rate'],
            'average_complexity': metadata['average_complexity'],
            'activity_span': str(activity_span),
            'interaction_breakdown': dict(metadata['interaction_types']),
            'recent_activity': len(recent_interactions),
            'synchronization_events': len(metadata['synchronization_events'])
        }
        
        return statistics
    
    def get_system_metrics(self) -> Dict[str, Any]:
        """Get overall system performance metrics"""
        
        with self.lock:
            # Calculate success rate
            total_challenges = (self.performance_metrics['successful_challenges'] + 
                              self.performance_metrics['failed_challenges'])
            
            if total_challenges > 0:
                system_success_rate = (self.performance_metrics['successful_challenges'] / 
                                     total_challenges)
            else:
                system_success_rate = 0.0
            
            # Get recent coherence measurements
            recent_coherence = list(self.coherence_timeline)[-10:] if self.coherence_timeline else []
            
            avg_coherence = 0.0
            if recent_coherence:
                avg_coherence = sum(r['coherence_value'] for r in recent_coherence) / len(recent_coherence)
            
            metrics = {
                'total_interactions': self.performance_metrics['total_interactions'],
                'successful_challenges': self.performance_metrics['successful_challenges'],
                'failed_challenges': self.performance_metrics['failed_challenges'],
                'system_success_rate': system_success_rate,
                'active_observers': len(self.observer_metadata),
                'average_system_coherence': avg_coherence,
                'active_sessions': len(self.active_sessions),
                'sync_events_count': len(self.sync_events),
                'coherence_measurements': len(self.coherence_timeline)
            }
            
            return metrics
    
    def export_observer_data(self, user_id: int) -> Dict[str, Any]:
        """Export complete observer data for analysis"""
        
        if user_id not in self.observer_metadata:
            return {'error': 'Observer not found'}
        
        return {
            'metadata': self.observer_metadata[user_id],
            'interaction_history': self.get_observer_history(user_id),
            'statistics': self.get_observer_statistics(user_id),
            'export_timestamp': datetime.now().isoformat()
        }
    
    def cleanup_old_data(self, retention_days: int = 30):
        """Clean up old interaction data"""
        
        cutoff_time = time.time() - (retention_days * 24 * 3600)
        
        with self.lock:
            # Clean up old interactions
            for user_id in list(self.observer_interactions.keys()):
                interactions = self.observer_interactions[user_id]
                
                # Keep only recent interactions
                recent_interactions = deque(
                    [i for i in interactions if i['timestamp'] > cutoff_time],
                    maxlen=self.max_history_per_observer
                )
                
                if recent_interactions:
                    self.observer_interactions[user_id] = recent_interactions
                else:
                    # Remove observer if no recent activity
                    del self.observer_interactions[user_id]
                    if user_id in self.observer_metadata:
                        del self.observer_metadata[user_id]
            
            # Clean up old sync events
            self.sync_events = deque(
                [e for e in self.sync_events if e['timestamp'] > cutoff_time],
                maxlen=500
            )
            
            # Clean up old coherence measurements
            self.coherence_timeline = deque(
                [c for c in self.coherence_timeline if c['timestamp'] > cutoff_time],
                maxlen=200
            )
            
            # Clear sync status cache
            self.sync_status_cache.clear()
            
            logger.info(f"Cleaned up observer data older than {retention_days} days")
    
    def log_observer_state(self, user_id: int, challenge_text: str):
        """
        Log observer state with phase shift calculation
        
        Args:
            user_id: Telegram user ID
            challenge_text: The challenge text submitted
        """
        
        with self.lock:
            current_time = time.time()
            
            # Calculate Δφ (phase shift) between challenges
            delta_phi = 0.0
            if user_id in self.observer_last_challenge:
                time_diff = current_time - self.observer_last_challenge[user_id]['timestamp']
                # Phase shift based on time difference (radians)
                delta_phi = math.sin(time_diff / 3600) * math.pi  # Hourly cycle modulation
            
            # Get username if available from recent interactions
            username = "unknown"
            recent_interactions = list(self.observer_interactions[user_id])
            if recent_interactions:
                # Try to extract username from recent interaction data
                username = f"observer_{user_id}"
            
            # Create observer state log entry
            observer_entry = {
                'timestamp': current_time,
                'datetime': datetime.fromtimestamp(current_time).isoformat(),
                'user_id': user_id,
                'username': username,
                'challenge_text': challenge_text[:100] + '...' if len(challenge_text) > 100 else challenge_text,
                'delta_phi': delta_phi,
                'tau_eff': 1.0,  # Default effective timing
                'omega_obs': delta_phi / 1.0 if delta_phi != 0 else 0.0  # Ω_obs = Δφ / τ_eff
            }
            
            # Save to observer log file
            self._save_observer_log(observer_entry)
            
            # Update last challenge time
            self.observer_last_challenge[user_id] = {
                'timestamp': current_time,
                'challenge': challenge_text
            }
            
            logger.info(f"Observer state logged for {user_id}: Δφ={delta_phi:.4f}, Ω_obs={observer_entry['omega_obs']:.4f}")
    
    def _save_observer_log(self, entry: Dict[str, Any]):
        """Save observer log entry to JSON file"""
        
        log_file = 'logs/observer_log.json'
        
        try:
            # Load existing log
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    log_data = json.load(f)
            else:
                log_data = []
            
            # Append new entry
            log_data.append(entry)
            
            # Keep only last 1000 entries
            if len(log_data) > 1000:
                log_data = log_data[-1000:]
            
            # Save updated log
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
                
            logger.debug(f"Observer log saved to {log_file}")
            
        except Exception as e:
            logger.error(f"Failed to save observer log: {str(e)}")
    
    def get_recent_observer_logs(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get recent observer log entries"""
        
        log_file = 'logs/observer_log.json'
        
        try:
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    log_data = json.load(f)
                return log_data[-limit:] if log_data else []
            else:
                return []
        except Exception as e:
            logger.error(f"Failed to read observer log: {str(e)}")
            return []
    
    def get_coherence_trend(self, observer_id: int) -> str:
        """
        Ω_Lens – Coherence Visualizer
        Analyzes observer's Δφ trends and coherence patterns
        
        Args:
            observer_id: Observer identifier
            
        Returns:
            Formatted coherence trend message
        """
        
        log_file = 'logs/observer_log.json'
        
        try:
            if not os.path.exists(log_file):
                return f"Observer #{observer_id} | No coherence data available"
            
            with open(log_file, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
            
            # Filter entries for this observer
            observer_entries = [entry for entry in log_data if entry['user_id'] == observer_id]
            
            if len(observer_entries) < 2:
                return f"Observer #{observer_id} | Insufficient data for trend analysis"
            
            # Get last 10 Δφ values
            recent_entries = observer_entries[-10:]
            delta_phi_values = [entry['delta_phi'] for entry in recent_entries]
            
            # Calculate statistics
            mean_delta_phi = sum(delta_phi_values) / len(delta_phi_values)
            variance = sum((x - mean_delta_phi) ** 2 for x in delta_phi_values) / len(delta_phi_values)
            std_dev = math.sqrt(variance)
            
            # Calculate drift percentage (change from first to last)
            if len(delta_phi_values) >= 2:
                drift_rate = ((delta_phi_values[-1] - delta_phi_values[0]) / max(abs(delta_phi_values[0]), 0.001)) * 100
            else:
                drift_rate = 0.0
            
            # Generate trend message
            trend_msg = f"Observer #{observer_id} | Δφ Mean: {mean_delta_phi:.4f}, Drift: {drift_rate:.1f}%"
            
            # Add coherence classification
            if std_dev < 0.1:
                trend_msg += " [STABLE]"
            elif std_dev < 0.3:
                trend_msg += " [MODERATE]"
            else:
                trend_msg += " [VOLATILE]"
            
            logger.info(f"Coherence trend calculated for observer {observer_id}: drift={drift_rate:.1f}%")
            
            return trend_msg
            
        except Exception as e:
            logger.error(f"Error calculating coherence trend: {str(e)}")
            return f"Observer #{observer_id} | Coherence analysis failed: {str(e)}"
