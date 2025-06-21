"""
NeuroFrame – Observer Memory Cache
Stores and analyzes observer behavioral patterns and coherence fingerprints
"""

import json
import os
import hashlib
import time
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from collections import deque

logger = logging.getLogger(__name__)

class ObserverMemory:
    """
    NeuroFrame – Observer Memory Cache
    Creates and maintains observer behavioral fingerprints and memory patterns
    """
    
    def __init__(self, memory_dir: str = 'memory'):
        """Initialize NeuroFrame memory system"""
        
        self.memory_dir = memory_dir
        self.observer_fingerprints = {}
        self.fingerprint_history = {}
        
        # Ensure memory directory exists
        os.makedirs(memory_dir, exist_ok=True)
        
        # Fingerprint parameters
        self.fingerprint_weights = {
            'challenge_complexity': 0.25,
            'response_time': 0.20,
            'coherence_patterns': 0.30,
            'symbol_usage': 0.15,
            'interaction_rhythm': 0.10
        }
        
        logger.info("NeuroFrame Observer Memory initialized")
    
    def process_observer_memory(self, user_id: int, challenge_text: str, 
                               challenge_data: Dict[str, Any], 
                               processing_time: float) -> Dict[str, Any]:
        """
        Process and update observer memory with new interaction data
        
        Args:
            user_id: Observer identifier
            challenge_text: Original challenge text
            challenge_data: Processed challenge analysis
            processing_time: Time taken to process challenge
            
        Returns:
            Memory analysis results including fingerprint changes
        """
        
        try:
            # Load existing memory
            memory_data = self._load_observer_memory(user_id)
            
            # Create current interaction fingerprint
            current_fingerprint = self._generate_fingerprint(
                challenge_text, challenge_data, processing_time
            )
            
            # Update memory with new data
            updated_memory = self._update_memory_cache(
                memory_data, challenge_text, challenge_data, 
                processing_time, current_fingerprint
            )
            
            # Analyze fingerprint changes
            fingerprint_analysis = self._analyze_fingerprint_changes(
                user_id, current_fingerprint, memory_data.get('fingerprint_history', [])
            )
            
            # Save updated memory
            self._save_observer_memory(user_id, updated_memory)
            
            # Check for dramatic fingerprint changes
            alert_triggered = fingerprint_analysis.get('dramatic_change', False)
            
            memory_result = {
                'fingerprint': current_fingerprint,
                'fingerprint_change': fingerprint_analysis.get('change_magnitude', 0.0),
                'alert_triggered': alert_triggered,
                'memory_updated': True,
                'interaction_count': updated_memory.get('total_interactions', 0)
            }
            
            if alert_triggered:
                logger.warning(f"NeuroFrame: Dramatic fingerprint change detected for observer {user_id}")
            
            return memory_result
            
        except Exception as e:
            logger.error(f"Error processing observer memory: {str(e)}")
            return {'error': str(e), 'memory_updated': False}
    
    def _load_observer_memory(self, user_id: int) -> Dict[str, Any]:
        """Load observer memory from JSON file"""
        
        memory_file = os.path.join(self.memory_dir, f"user_{user_id}.json")
        
        if os.path.exists(memory_file):
            try:
                with open(memory_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading memory for user {user_id}: {str(e)}")
        
        # Return default memory structure
        return {
            'user_id': user_id,
            'created_at': datetime.now().isoformat(),
            'total_interactions': 0,
            'recent_challenges': [],
            'coherence_trends': [],
            'auth_match_values': [],
            'fingerprint_history': [],
            'behavioral_patterns': {}
        }
    
    def _generate_fingerprint(self, challenge_text: str, 
                            challenge_data: Dict[str, Any], 
                            processing_time: float) -> str:
        """Generate behavioral fingerprint hash for current interaction"""
        
        try:
            # Extract fingerprint components
            complexity = challenge_data.get('complexity', 0.5)
            semantic_density = challenge_data.get('semantic_density', 0.5)
            challenge_type = challenge_data.get('type', 'general')
            word_count = challenge_data.get('word_count', 0)
            
            # Count RFT symbols usage
            rft_symbols = ['τ_eff', 'tau_eff', 'Δφ', 'delta_phi', 'Ω_obs', 'omega_obs', 'χ_Liam', 'chi_liam']
            symbol_count = sum(1 for symbol in rft_symbols if symbol in challenge_text.lower())
            
            # Create fingerprint data
            fingerprint_data = {
                'complexity_bucket': round(complexity * 10),
                'density_bucket': round(semantic_density * 10),
                'type_hash': hashlib.md5(challenge_type.encode()).hexdigest()[:8],
                'word_count_bucket': min(word_count // 10, 10),
                'symbol_usage': symbol_count,
                'processing_time_bucket': round(processing_time * 10),
                'text_entropy': len(set(challenge_text.lower())) / max(len(challenge_text), 1)
            }
            
            # Create weighted fingerprint string
            fingerprint_str = f"{fingerprint_data['complexity_bucket']}-{fingerprint_data['density_bucket']}-{fingerprint_data['type_hash']}-{fingerprint_data['word_count_bucket']}-{fingerprint_data['symbol_usage']}-{fingerprint_data['processing_time_bucket']}-{round(fingerprint_data['text_entropy'] * 100)}"
            
            # Generate hash
            fingerprint_hash = hashlib.sha256(fingerprint_str.encode()).hexdigest()[:16]
            
            return fingerprint_hash
            
        except Exception as e:
            logger.error(f"Error generating fingerprint: {str(e)}")
            return "default_fingerprint"
    
    def _update_memory_cache(self, memory_data: Dict[str, Any], 
                           challenge_text: str, challenge_data: Dict[str, Any],
                           processing_time: float, fingerprint: str) -> Dict[str, Any]:
        """Update observer memory cache with new interaction data"""
        
        current_time = datetime.now().isoformat()
        
        # Update interaction count
        memory_data['total_interactions'] += 1
        memory_data['last_updated'] = current_time
        
        # Add to recent challenges (keep last 20)
        challenge_entry = {
            'timestamp': current_time,
            'text_preview': challenge_text[:100] + '...' if len(challenge_text) > 100 else challenge_text,
            'type': challenge_data.get('type', 'general'),
            'complexity': challenge_data.get('complexity', 0.5),
            'processing_time': processing_time,
            'fingerprint': fingerprint
        }
        
        memory_data['recent_challenges'].append(challenge_entry)
        if len(memory_data['recent_challenges']) > 20:
            memory_data['recent_challenges'] = memory_data['recent_challenges'][-20:]
        
        # Update coherence trends
        coherence_trend = {
            'timestamp': current_time,
            'complexity': challenge_data.get('complexity', 0.5),
            'semantic_density': challenge_data.get('semantic_density', 0.5),
            'entropy': challenge_data.get('entropy', 0.5)
        }
        
        memory_data['coherence_trends'].append(coherence_trend)
        if len(memory_data['coherence_trends']) > 50:
            memory_data['coherence_trends'] = memory_data['coherence_trends'][-50:]
        
        # Update fingerprint history
        memory_data['fingerprint_history'].append({
            'timestamp': current_time,
            'fingerprint': fingerprint
        })
        if len(memory_data['fingerprint_history']) > 100:
            memory_data['fingerprint_history'] = memory_data['fingerprint_history'][-100:]
        
        # Update behavioral patterns
        if 'behavioral_patterns' not in memory_data:
            memory_data['behavioral_patterns'] = {}
        
        patterns = memory_data['behavioral_patterns']
        challenge_type = challenge_data.get('type', 'general')
        
        if challenge_type not in patterns:
            patterns[challenge_type] = {'count': 0, 'avg_complexity': 0.0}
        
        # Update type-specific patterns
        type_pattern = patterns[challenge_type]
        type_pattern['count'] += 1
        current_complexity = challenge_data.get('complexity', 0.5)
        type_pattern['avg_complexity'] = ((type_pattern['avg_complexity'] * (type_pattern['count'] - 1)) + current_complexity) / type_pattern['count']
        
        return memory_data
    
    def _analyze_fingerprint_changes(self, user_id: int, current_fingerprint: str, 
                                   fingerprint_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze fingerprint changes for dramatic shifts"""
        
        analysis = {
            'change_magnitude': 0.0,
            'dramatic_change': False,
            'pattern_shift': False
        }
        
        try:
            if len(fingerprint_history) < 3:
                return analysis
            
            # Get recent fingerprints
            recent_fingerprints = [entry['fingerprint'] for entry in fingerprint_history[-5:]]
            
            # Calculate fingerprint similarity
            similarity_scores = []
            for prev_fingerprint in recent_fingerprints:
                similarity = self._calculate_fingerprint_similarity(current_fingerprint, prev_fingerprint)
                similarity_scores.append(similarity)
            
            avg_similarity = sum(similarity_scores) / len(similarity_scores)
            change_magnitude = 1.0 - avg_similarity
            
            analysis['change_magnitude'] = change_magnitude
            
            # Check for dramatic change (threshold: 0.7)
            if change_magnitude > 0.7:
                analysis['dramatic_change'] = True
            
            # Check for pattern shift (fingerprint hasn't appeared in recent history)
            if current_fingerprint not in recent_fingerprints:
                analysis['pattern_shift'] = True
            
        except Exception as e:
            logger.error(f"Error analyzing fingerprint changes: {str(e)}")
        
        return analysis
    
    def _calculate_fingerprint_similarity(self, fp1: str, fp2: str) -> float:
        """Calculate similarity between two fingerprints"""
        
        if fp1 == fp2:
            return 1.0
        
        # Simple character-based similarity
        common_chars = sum(1 for a, b in zip(fp1, fp2) if a == b)
        max_length = max(len(fp1), len(fp2))
        
        return common_chars / max_length if max_length > 0 else 0.0
    
    def _save_observer_memory(self, user_id: int, memory_data: Dict[str, Any]):
        """Save observer memory to JSON file"""
        
        memory_file = os.path.join(self.memory_dir, f"user_{user_id}.json")
        
        try:
            with open(memory_file, 'w', encoding='utf-8') as f:
                json.dump(memory_data, f, indent=2, ensure_ascii=False)
            
            logger.debug(f"Observer memory saved for user {user_id}")
            
        except Exception as e:
            logger.error(f"Failed to save observer memory: {str(e)}")
    
    def get_observer_summary(self, user_id: int) -> Dict[str, Any]:
        """Get summary of observer memory and patterns"""
        
        memory_data = self._load_observer_memory(user_id)
        
        summary = {
            'user_id': user_id,
            'total_interactions': memory_data.get('total_interactions', 0),
            'behavioral_patterns': memory_data.get('behavioral_patterns', {}),
            'recent_fingerprints': len(memory_data.get('fingerprint_history', [])),
            'memory_file_exists': os.path.exists(os.path.join(self.memory_dir, f"user_{user_id}.json"))
        }
        
        return summary