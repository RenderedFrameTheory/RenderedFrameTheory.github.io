"""
RFT Engine - Core Rendered Frame Theory calculation and processing engine
Implements the core equation: Ω = (Ω_obs · χ_Liam) / (Δφ · Υ)
"""

import numpy as np
import math
import time
import random
from datetime import datetime
from typing import Dict, List, Tuple, Any
import logging

logger = logging.getLogger(__name__)

class RFTEngine:
    """
    Core RFT (Rendered Frame Theory) calculation engine
    Processes observer-based rendering using the fundamental RFT equation
    """
    
    def __init__(self):
        """Initialize RFT Engine with base parameters"""
        self.base_parameters = {
            'omega_obs_base': 1.618,  # Golden ratio base for observer state
            'chi_liam_base': 2.718,   # Euler's number for coherence
            'delta_phi_base': 3.14159, # Pi for phase differential
            'upsilon_base': 1.414,    # Square root of 2 for temporal scaling
            'tau_eff_base': 1.0       # Base effective timing
        }
        
        self.current_parameters = self.base_parameters.copy()
        self.calculation_history = []
        self.observer_states = {}
        
        # RFT Constants
        self.COHERENCE_THRESHOLD = 0.707  # sqrt(2)/2
        self.PHASE_STABILITY_LIMIT = 2 * math.pi
        self.TEMPORAL_VARIANCE_MAX = 10.0
        self.OBSERVER_SYNC_TOLERANCE = 0.05
        
        logger.info("RFT Engine initialized with base parameters")
    
    def initialize(self):
        """Initialize RFT engine systems"""
        logger.info("Initializing RFT calculation matrices...")
        
        # Initialize observer state tracking
        self.observer_states = {}
        
        # Reset calculation history
        self.calculation_history = []
        
        # Calibrate base parameters
        self._calibrate_base_parameters()
        
        logger.info("RFT Engine initialization complete")
    
    def _calibrate_base_parameters(self):
        """Calibrate base parameters for current system state"""
        current_time = time.time()
        
        # Apply temporal modulation to base parameters
        time_factor = math.sin(current_time / 86400) * 0.1  # Daily cycle modulation
        
        self.current_parameters['omega_obs_base'] *= (1 + time_factor)
        self.current_parameters['chi_liam_base'] *= (1 + time_factor * 0.5)
        
        logger.debug(f"Base parameters calibrated with time factor: {time_factor:.4f}")
    
    def calculate_rft_parameters(self, challenge_data: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate RFT parameters for a given challenge
        
        Args:
            challenge_data: Processed challenge information
            
        Returns:
            Dictionary containing calculated RFT parameters
        """
        user_id = challenge_data.get('user_id', 0)
        challenge_type = challenge_data.get('type', 'general')
        complexity = challenge_data.get('complexity', 0.5)
        semantic_density = challenge_data.get('semantic_density', 0.5)
        
        # Calculate observer state (Ω_obs)
        omega_obs = self._calculate_observer_state(user_id, challenge_data)
        
        # Calculate coherence coefficient (χ_Liam)
        chi_liam = self._calculate_coherence_coefficient(challenge_type, complexity)
        
        # Calculate phase differential (Δφ)
        delta_phi = self._calculate_phase_differential(semantic_density, challenge_data)
        
        # Calculate temporal scaling factor (Υ)
        upsilon = self._calculate_temporal_scaling(user_id, challenge_data)
        
        # Calculate effective observer timing (τ_eff)
        tau_eff = self._calculate_effective_timing(omega_obs, chi_liam, delta_phi, upsilon)
        
        rft_params = {
            'omega_obs': omega_obs,
            'chi_liam': chi_liam,
            'delta_phi': delta_phi,
            'upsilon': upsilon,
            'tau_eff': tau_eff,
            'calculation_timestamp': time.time(),
            'observer_id': user_id
        }
        
        # Store in calculation history
        self.calculation_history.append(rft_params.copy())
        
        logger.info(f"RFT parameters calculated for observer {user_id}: Ω_obs={omega_obs:.4f}, χ_Liam={chi_liam:.4f}")
        
        return rft_params
    
    def _calculate_observer_state(self, user_id: int, challenge_data: Dict[str, Any]) -> float:
        """Calculate observer state measurement (Ω_obs)"""
        
        # Get or initialize observer state
        if user_id not in self.observer_states:
            self.observer_states[user_id] = {
                'base_coherence': random.uniform(0.8, 1.2),
                'interaction_count': 0,
                'challenge_history': [],
                'synchronization_level': 1.0
            }
        
        observer = self.observer_states[user_id]
        observer['interaction_count'] += 1
        
        # Base observer measurement
        omega_obs = self.current_parameters['omega_obs_base'] * observer['base_coherence']
        
        # Apply interaction experience modifier
        experience_factor = 1 + (observer['interaction_count'] * 0.01)
        omega_obs *= min(experience_factor, 2.0)  # Cap at 2x base
        
        # Apply challenge complexity modifier
        complexity = challenge_data.get('complexity', 0.5)
        complexity_modifier = 0.8 + (complexity * 0.4)  # Range: 0.8 to 1.2
        omega_obs *= complexity_modifier
        
        # Apply temporal coherence
        current_time = time.time()
        temporal_coherence = math.cos(current_time / 3600) * 0.1 + 1  # Hourly variation
        omega_obs *= temporal_coherence
        
        # Update observer state
        observer['synchronization_level'] = min(omega_obs / self.current_parameters['omega_obs_base'], 2.0)
        
        return omega_obs
    
    def _calculate_coherence_coefficient(self, challenge_type: str, complexity: float) -> float:
        """Calculate coherence coefficient (χ_Liam)"""
        
        # Base coherence from Liam parameter
        chi_liam = self.current_parameters['chi_liam_base']
        
        # Type-specific modifiers
        type_modifiers = {
            'cognitive': 1.2,
            'theoretical': 1.1,
            'perceptual': 1.15,
            'temporal': 1.3,
            'quantum': 1.25,
            'consciousness': 1.4,
            'general': 1.0
        }
        
        modifier = type_modifiers.get(challenge_type, 1.0)
        chi_liam *= modifier
        
        # Apply complexity scaling
        complexity_scaling = 0.7 + (complexity * 0.6)  # Range: 0.7 to 1.3
        chi_liam *= complexity_scaling
        
        # Apply coherence stability check
        if chi_liam > self.COHERENCE_THRESHOLD * 4:
            chi_liam *= 0.9  # Prevent excessive coherence
        
        return chi_liam
    
    def _calculate_phase_differential(self, semantic_density: float, challenge_data: Dict[str, Any]) -> float:
        """Calculate phase differential (Δφ)"""
        
        # Base phase differential
        delta_phi = self.current_parameters['delta_phi_base']
        
        # Apply semantic density modulation
        semantic_factor = semantic_density * 2  # Scale up density impact
        delta_phi *= (1 + semantic_factor * 0.2)
        
        # Apply challenge entropy
        entropy = challenge_data.get('entropy', 0.5)
        entropy_modifier = 1 + (entropy - 0.5) * 0.3
        delta_phi *= entropy_modifier
        
        # Apply temporal phase shift
        current_time = time.time()
        phase_shift = math.sin(current_time / 1800) * 0.5  # 30-minute cycle
        delta_phi += phase_shift
        
        # Ensure phase stays within stability limits
        if delta_phi > self.PHASE_STABILITY_LIMIT:
            delta_phi = delta_phi % self.PHASE_STABILITY_LIMIT
        
        return abs(delta_phi)  # Phase differential is always positive
    
    def _calculate_temporal_scaling(self, user_id: int, challenge_data: Dict[str, Any]) -> float:
        """Calculate temporal scaling factor (Υ)"""
        
        # Base temporal scaling
        upsilon = self.current_parameters['upsilon_base']
        
        # Apply observer synchronization
        if user_id in self.observer_states:
            sync_level = self.observer_states[user_id]['synchronization_level']
            upsilon *= sync_level
        
        # Apply challenge urgency (based on processing requirements)
        urgency = challenge_data.get('urgency', 0.5)
        urgency_scaling = 0.8 + (urgency * 0.4)
        upsilon *= urgency_scaling
        
        # Apply temporal variance limits
        variance = random.uniform(-0.1, 0.1)
        upsilon *= (1 + variance)
        
        # Ensure scaling stays within acceptable bounds
        upsilon = max(0.1, min(upsilon, self.TEMPORAL_VARIANCE_MAX))
        
        return upsilon
    
    def _calculate_effective_timing(self, omega_obs: float, chi_liam: float, 
                                  delta_phi: float, upsilon: float) -> float:
        """Calculate effective observer timing (τ_eff)"""
        
        # Calculate primary RFT equation components
        numerator = omega_obs * chi_liam
        denominator = delta_phi * upsilon
        
        # Prevent division by zero
        if denominator == 0:
            denominator = 0.001
        
        # Calculate base effective timing
        tau_eff = numerator / denominator
        
        # Apply temporal coherence correction
        coherence_factor = min(chi_liam / self.current_parameters['chi_liam_base'], 2.0)
        tau_eff *= coherence_factor
        
        # Apply observer timing normalization
        tau_eff *= self.base_parameters['tau_eff_base']
        
        return tau_eff
    
    def render_frame(self, rft_params: Dict[str, float], challenge_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Render frame based on RFT parameters and challenge data
        Core implementation of: Ω = (Ω_obs · χ_Liam) / (Δφ · Υ)
        """
        
        # Extract RFT parameters
        omega_obs = rft_params['omega_obs']
        chi_liam = rft_params['chi_liam']
        delta_phi = rft_params['delta_phi']
        upsilon = rft_params['upsilon']
        tau_eff = rft_params['tau_eff']
        
        # Calculate core RFT equation: Ω = (Ω_obs · χ_Liam) / (Δφ · Υ)
        omega_result = (omega_obs * chi_liam) / (delta_phi * upsilon)
        
        # Calculate frame stability
        stability = self._calculate_frame_stability(rft_params)
        
        # Calculate rendering confidence
        confidence = self._calculate_rendering_confidence(omega_result, stability, tau_eff)
        
        # Generate frame characteristics
        frame_characteristics = self._generate_frame_characteristics(omega_result, rft_params, challenge_data)
        
        # Calculate observer alignment
        observer_alignment = self._calculate_observer_alignment(rft_params, challenge_data)
        
        rendered_frame = {
            'omega_result': omega_result,
            'stability': stability,
            'confidence': confidence,
            'tau_eff': tau_eff,
            'frame_characteristics': frame_characteristics,
            'observer_alignment': observer_alignment,
            'rendering_timestamp': time.time(),
            'rft_equation_components': {
                'numerator': omega_obs * chi_liam,
                'denominator': delta_phi * upsilon,
                'equation_balance': (omega_obs * chi_liam) / max(delta_phi * upsilon, 0.001)
            }
        }
        
        logger.info(f"Frame rendered: Ω={omega_result:.4f}, Stability={stability:.2%}, Confidence={confidence:.2%}")
        
        return rendered_frame
    
    def _calculate_frame_stability(self, rft_params: Dict[str, float]) -> float:
        """Calculate rendered frame stability"""
        
        omega_obs = rft_params['omega_obs']
        chi_liam = rft_params['chi_liam']
        delta_phi = rft_params['delta_phi']
        upsilon = rft_params['upsilon']
        
        # Calculate parameter variance from base values
        obs_variance = abs(omega_obs - self.current_parameters['omega_obs_base']) / self.current_parameters['omega_obs_base']
        coherence_variance = abs(chi_liam - self.current_parameters['chi_liam_base']) / self.current_parameters['chi_liam_base']
        phase_variance = abs(delta_phi - self.current_parameters['delta_phi_base']) / self.current_parameters['delta_phi_base']
        temporal_variance = abs(upsilon - self.current_parameters['upsilon_base']) / self.current_parameters['upsilon_base']
        
        # Calculate overall stability (inverse of variance)
        total_variance = (obs_variance + coherence_variance + phase_variance + temporal_variance) / 4
        stability = max(0, 1 - total_variance)
        
        return stability
    
    def _calculate_rendering_confidence(self, omega_result: float, stability: float, tau_eff: float) -> float:
        """Calculate confidence in the rendered frame"""
        
        # Base confidence from omega result magnitude
        omega_confidence = min(abs(omega_result) / 2, 1.0)
        
        # Stability contribution
        stability_confidence = stability
        
        # Timing effectiveness contribution
        timing_confidence = min(tau_eff / 2, 1.0)
        
        # Combined confidence calculation
        confidence = (omega_confidence * 0.4 + stability_confidence * 0.35 + timing_confidence * 0.25)
        
        return confidence
    
    def _generate_frame_characteristics(self, omega_result: float, rft_params: Dict[str, float], 
                                      challenge_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate frame characteristics based on rendering results"""
        
        characteristics = {
            'coherence_level': min(rft_params['chi_liam'] / self.current_parameters['chi_liam_base'], 2.0),
            'temporal_alignment': rft_params['tau_eff'],
            'phase_coherence': math.cos(rft_params['delta_phi']),
            'observer_resonance': rft_params['omega_obs'] / self.current_parameters['omega_obs_base'],
            'complexity_resolution': omega_result,
            'frame_type': self._determine_frame_type(omega_result, rft_params),
            'rendering_quality': self._assess_rendering_quality(omega_result, rft_params)
        }
        
        return characteristics
    
    def _determine_frame_type(self, omega_result: float, rft_params: Dict[str, float]) -> str:
        """Determine the type of rendered frame based on parameters"""
        
        if omega_result > 2.0:
            return "high_coherence"
        elif omega_result > 1.0:
            return "stable_coherence" 
        elif omega_result > 0.5:
            return "moderate_coherence"
        else:
            return "low_coherence"
    
    def _assess_rendering_quality(self, omega_result: float, rft_params: Dict[str, float]) -> str:
        """Assess the quality of the rendered frame"""
        
        stability = self._calculate_frame_stability(rft_params)
        
        if stability > 0.8 and omega_result > 1.5:
            return "excellent"
        elif stability > 0.6 and omega_result > 1.0:
            return "good"
        elif stability > 0.4 and omega_result > 0.5:
            return "fair"
        else:
            return "poor"
    
    def _calculate_observer_alignment(self, rft_params: Dict[str, float], 
                                    challenge_data: Dict[str, Any]) -> float:
        """Calculate observer alignment with rendered frame"""
        
        user_id = rft_params.get('observer_id', 0)
        
        if user_id in self.observer_states:
            observer = self.observer_states[user_id]
            
            # Base alignment from synchronization level
            base_alignment = observer['synchronization_level']
            
            # Adjust for challenge compatibility
            challenge_type = challenge_data.get('type', 'general')
            type_alignment = self._get_observer_type_alignment(user_id, challenge_type)
            
            # Combined alignment
            alignment = (base_alignment * 0.7 + type_alignment * 0.3)
            
            return min(alignment, 1.0)
        
        return 0.5  # Default alignment for new observers
    
    def _get_observer_type_alignment(self, user_id: int, challenge_type: str) -> float:
        """Get observer alignment for specific challenge types"""
        
        # This would be enhanced with learning from observer history
        # For now, use base alignment with some variation
        base_alignment = 0.8
        type_variance = random.uniform(-0.2, 0.2)
        
        return max(0.1, min(base_alignment + type_variance, 1.0))
    
    def get_current_parameters(self) -> Dict[str, float]:
        """Get current RFT parameters"""
        return self.current_parameters.copy()
    
    def calculate_system_coherence(self) -> float:
        """Calculate overall system coherence"""
        
        if not self.calculation_history:
            return 0.5
        
        # Get recent calculations
        recent_calculations = self.calculation_history[-10:]  # Last 10 calculations
        
        # Calculate average coherence from recent chi_liam values
        avg_coherence = np.mean([calc['chi_liam'] for calc in recent_calculations])
        base_coherence = self.current_parameters['chi_liam_base']
        
        # Normalize to 0-1 range
        system_coherence = min(avg_coherence / (base_coherence * 2), 1.0)
        
        return system_coherence
    
    def get_observer_state(self, user_id: int) -> Dict[str, Any]:
        """Get current observer state"""
        return self.observer_states.get(user_id, {})
    
    def update_observer_synchronization(self, user_id: int, sync_adjustment: float):
        """Update observer synchronization level"""
        if user_id in self.observer_states:
            current_sync = self.observer_states[user_id]['synchronization_level']
            new_sync = max(0.1, min(current_sync + sync_adjustment, 2.0))
            self.observer_states[user_id]['synchronization_level'] = new_sync
            
            logger.debug(f"Observer {user_id} synchronization updated: {current_sync:.3f} -> {new_sync:.3f}")
    
    def render_simulation(self, tau_eff: float, delta_phi: float, observer_id: int) -> str:
        """
        RFT Render Engine Upgrade - Simulation renderer
        
        Args:
            tau_eff: Effective timing in seconds
            delta_phi: Phase differential in radians
            observer_id: Observer identifier
            
        Returns:
            Formatted render result string
        """
        
        try:
            # Prevent division by zero
            if tau_eff == 0:
                tau_eff = 0.001
            
            # Calculate Ω_obs using: Ω_obs = Δφ / τ_eff
            omega_obs = delta_phi / tau_eff
            
            # Log the render simulation
            logger.info(f"Render simulation: τ_eff={tau_eff:.4f}s, Δφ={delta_phi:.4f}rad, Ω_obs={omega_obs:.4f}rad/s")
            
            # Format result string
            result = f"Render successful. Ω_obs = {omega_obs:.6f} rad/s for Observer #{observer_id}"
            
            return result
            
        except Exception as e:
            logger.error(f"Render simulation error: {str(e)}")
            return f"Render failed for Observer #{observer_id}: {str(e)}"
    
    def track_render_drift(self, observer_id: int) -> str:
        """
        SyncView – τ_eff Drift Tracker
        Analyzes observer's temporal effectiveness drift patterns
        
        Args:
            observer_id: Observer identifier
            
        Returns:
            Drift classification: STABLE / DRIFTING / UNSTABLE
        """
        
        try:
            # Get observer state
            if observer_id not in self.observer_states:
                return "UNKNOWN"
            
            observer = self.observer_states[observer_id]
            challenge_history = observer.get('challenge_history', [])
            
            if len(challenge_history) < 3:
                return "INSUFFICIENT_DATA"
            
            # Get recent τ_eff values from calculation history
            recent_calculations = [calc for calc in self.calculation_history[-20:] 
                                 if calc.get('observer_id') == observer_id]
            
            if len(recent_calculations) < 2:
                return "STABLE"  # Default for insufficient data
            
            tau_eff_values = [calc['tau_eff'] for calc in recent_calculations]
            
            # Calculate drift rate
            if len(tau_eff_values) >= 2:
                current_tau = tau_eff_values[-1]
                previous_tau = tau_eff_values[-2]
                
                if previous_tau != 0:
                    drift_rate = abs((current_tau - previous_tau) / previous_tau)
                else:
                    drift_rate = 0.0
                
                # Calculate overall variance
                mean_tau = sum(tau_eff_values) / len(tau_eff_values)
                variance = sum((x - mean_tau) ** 2 for x in tau_eff_values) / len(tau_eff_values)
                coefficient_of_variation = math.sqrt(variance) / mean_tau if mean_tau != 0 else 0
                
                # Classify drift
                if drift_rate < 0.05 and coefficient_of_variation < 0.1:
                    classification = "STABLE"
                elif drift_rate < 0.15 and coefficient_of_variation < 0.25:
                    classification = "DRIFTING"
                else:
                    classification = "UNSTABLE"
                
                logger.info(f"Render drift tracked for observer {observer_id}: {classification} (drift={drift_rate:.3f})")
                
                return classification
            
            return "STABLE"
            
        except Exception as e:
            logger.error(f"Error tracking render drift: {str(e)}")
            return "ERROR"
