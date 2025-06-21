"""
Configuration module for RFT Omega Bot
Contains all configurable parameters and constants
"""

import os
from typing import Dict, Any

class Config:
    """Configuration class for RFT Omega Bot"""
    
    def __init__(self):
        """Initialize configuration with default values and environment overrides"""
        
        # Bot Configuration
        self.BOT_NAME = "RFT Ωmega Bot"
        self.BOT_VERSION = "1.0.0"
        self.BOT_DESCRIPTION = "Challenge. Name It. It Will Render It."
        
        # Telegram Bot Settings
        self.TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '')
        self.POLLING_INTERVAL = int(os.getenv('POLLING_INTERVAL', '1'))
        self.POLLING_TIMEOUT = int(os.getenv('POLLING_TIMEOUT', '20'))
        
        # RFT Engine Configuration
        self.RFT_BASE_OMEGA_OBS = float(os.getenv('RFT_BASE_OMEGA_OBS', '1.618'))
        self.RFT_BASE_CHI_LIAM = float(os.getenv('RFT_BASE_CHI_LIAM', '2.718'))
        self.RFT_BASE_DELTA_PHI = float(os.getenv('RFT_BASE_DELTA_PHI', '3.14159'))
        self.RFT_BASE_UPSILON = float(os.getenv('RFT_BASE_UPSILON', '1.414'))
        self.RFT_BASE_TAU_EFF = float(os.getenv('RFT_BASE_TAU_EFF', '1.0'))
        
        # RFT Calculation Limits
        self.COHERENCE_THRESHOLD = float(os.getenv('COHERENCE_THRESHOLD', '0.707'))
        self.PHASE_STABILITY_LIMIT = float(os.getenv('PHASE_STABILITY_LIMIT', '6.28318'))  # 2π
        self.TEMPORAL_VARIANCE_MAX = float(os.getenv('TEMPORAL_VARIANCE_MAX', '10.0'))
        self.OBSERVER_SYNC_TOLERANCE = float(os.getenv('OBSERVER_SYNC_TOLERANCE', '0.05'))
        
        # Session Management
        self.SESSION_TIMEOUT = int(os.getenv('SESSION_TIMEOUT', '3600'))  # 1 hour
        self.MAX_CONCURRENT_SESSIONS = int(os.getenv('MAX_CONCURRENT_SESSIONS', '100'))
        self.SESSION_CLEANUP_INTERVAL = int(os.getenv('SESSION_CLEANUP_INTERVAL', '300'))  # 5 minutes
        
        # Challenge Processing Limits
        self.MAX_CHALLENGE_LENGTH = int(os.getenv('MAX_CHALLENGE_LENGTH', '1000'))
        self.MIN_CHALLENGE_LENGTH = int(os.getenv('MIN_CHALLENGE_LENGTH', '10'))
        self.MAX_PROCESSING_TIME = int(os.getenv('MAX_PROCESSING_TIME', '30'))  # seconds
        
        # Logging Configuration
        self.LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
        self.LOG_FILE = os.getenv('LOG_FILE', 'rft_bot.log')
        self.LOG_MAX_BYTES = int(os.getenv('LOG_MAX_BYTES', '10485760'))  # 10MB
        self.LOG_BACKUP_COUNT = int(os.getenv('LOG_BACKUP_COUNT', '5'))
        
        # Observer Tracking
        self.TRACK_OBSERVER_HISTORY = os.getenv('TRACK_OBSERVER_HISTORY', 'true').lower() == 'true'
        self.OBSERVER_HISTORY_LIMIT = int(os.getenv('OBSERVER_HISTORY_LIMIT', '100'))
        self.SYNC_STATUS_CACHE_TIME = int(os.getenv('SYNC_STATUS_CACHE_TIME', '300'))  # 5 minutes
        
        # Performance Settings
        self.ENABLE_THREADING = os.getenv('ENABLE_THREADING', 'true').lower() == 'true'
        self.MAX_WORKER_THREADS = int(os.getenv('MAX_WORKER_THREADS', '10'))
        self.MEMORY_LIMIT_MB = int(os.getenv('MEMORY_LIMIT_MB', '512'))
        
        # API Rate Limiting
        self.RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT_ENABLED', 'true').lower() == 'true'
        self.RATE_LIMIT_REQUESTS = int(os.getenv('RATE_LIMIT_REQUESTS', '10'))
        self.RATE_LIMIT_WINDOW = int(os.getenv('RATE_LIMIT_WINDOW', '60'))  # seconds
        
        # Development/Debug Settings
        self.DEBUG_MODE = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
        self.VERBOSE_LOGGING = os.getenv('VERBOSE_LOGGING', 'false').lower() == 'true'
        self.ENABLE_METRICS = os.getenv('ENABLE_METRICS', 'true').lower() == 'true'
        
        # Advanced RFT Settings
        self.ENABLE_ADAPTIVE_PARAMETERS = os.getenv('ENABLE_ADAPTIVE_PARAMETERS', 'true').lower() == 'true'
        self.PARAMETER_LEARNING_RATE = float(os.getenv('PARAMETER_LEARNING_RATE', '0.01'))
        self.COHERENCE_DECAY_RATE = float(os.getenv('COHERENCE_DECAY_RATE', '0.99'))
        
        # Challenge Type Weights
        self.CHALLENGE_TYPE_WEIGHTS = {
            'cognitive': float(os.getenv('WEIGHT_COGNITIVE', '1.2')),
            'theoretical': float(os.getenv('WEIGHT_THEORETICAL', '1.1')),
            'quantum': float(os.getenv('WEIGHT_QUANTUM', '1.25')),
            'temporal': float(os.getenv('WEIGHT_TEMPORAL', '1.3')),
            'perceptual': float(os.getenv('WEIGHT_PERCEPTUAL', '1.15')),
            'consciousness': float(os.getenv('WEIGHT_CONSCIOUSNESS', '1.4')),
            'observer': float(os.getenv('WEIGHT_OBSERVER', '1.35')),
            'synchronization': float(os.getenv('WEIGHT_SYNCHRONIZATION', '1.2')),
            'ai_alignment': float(os.getenv('WEIGHT_AI_ALIGNMENT', '1.1')),
            'general': float(os.getenv('WEIGHT_GENERAL', '1.0'))
        }
        
        # Response Generation Settings
        self.RESPONSE_MAX_LENGTH = int(os.getenv('RESPONSE_MAX_LENGTH', '4000'))
        self.INCLUDE_TECHNICAL_DETAILS = os.getenv('INCLUDE_TECHNICAL_DETAILS', 'true').lower() == 'true'
        self.INCLUDE_OBSERVER_GUIDANCE = os.getenv('INCLUDE_OBSERVER_GUIDANCE', 'true').lower() == 'true'
        self.RANDOMIZE_TEMPLATES = os.getenv('RANDOMIZE_TEMPLATES', 'true').lower() == 'true'
        
        # Data Storage Settings
        self.ENABLE_DATA_PERSISTENCE = os.getenv('ENABLE_DATA_PERSISTENCE', 'false').lower() == 'true'
        self.DATA_STORAGE_PATH = os.getenv('DATA_STORAGE_PATH', './data')
        self.BACKUP_INTERVAL = int(os.getenv('BACKUP_INTERVAL', '3600'))  # 1 hour
        
        # Security Settings
        self.ENABLE_USER_VALIDATION = os.getenv('ENABLE_USER_VALIDATION', 'true').lower() == 'true'
        self.MAX_REQUESTS_PER_USER = int(os.getenv('MAX_REQUESTS_PER_USER', '50'))
        self.USER_COOLDOWN_PERIOD = int(os.getenv('USER_COOLDOWN_PERIOD', '60'))  # seconds
        
        # Feature Flags
        self.ENABLE_EXPERIMENTAL_FEATURES = os.getenv('ENABLE_EXPERIMENTAL_FEATURES', 'false').lower() == 'true'
        self.ENABLE_ADVANCED_ANALYSIS = os.getenv('ENABLE_ADVANCED_ANALYSIS', 'true').lower() == 'true'
        self.ENABLE_OBSERVER_LEARNING = os.getenv('ENABLE_OBSERVER_LEARNING', 'true').lower() == 'true'
        
    def get_rft_base_parameters(self) -> Dict[str, float]:
        """Get base RFT parameters as dictionary"""
        return {
            'omega_obs_base': self.RFT_BASE_OMEGA_OBS,
            'chi_liam_base': self.RFT_BASE_CHI_LIAM,
            'delta_phi_base': self.RFT_BASE_DELTA_PHI,
            'upsilon_base': self.RFT_BASE_UPSILON,
            'tau_eff_base': self.RFT_BASE_TAU_EFF
        }
    
    def get_calculation_limits(self) -> Dict[str, float]:
        """Get RFT calculation limits as dictionary"""
        return {
            'coherence_threshold': self.COHERENCE_THRESHOLD,
            'phase_stability_limit': self.PHASE_STABILITY_LIMIT,
            'temporal_variance_max': self.TEMPORAL_VARIANCE_MAX,
            'observer_sync_tolerance': self.OBSERVER_SYNC_TOLERANCE
        }
    
    def get_challenge_type_weights(self) -> Dict[str, float]:
        """Get challenge type weights"""
        return self.CHALLENGE_TYPE_WEIGHTS.copy()
    
    def validate_configuration(self) -> Dict[str, Any]:
        """Validate configuration settings and return validation results"""
        
        validation_results = {
            'valid': True,
            'errors': [],
            'warnings': []
        }
        
        # Validate required settings
        if not self.TELEGRAM_BOT_TOKEN:
            validation_results['valid'] = False
            validation_results['errors'].append('TELEGRAM_BOT_TOKEN is required')
        
        # Validate numeric ranges
        if self.COHERENCE_THRESHOLD <= 0 or self.COHERENCE_THRESHOLD > 1:
            validation_results['warnings'].append('COHERENCE_THRESHOLD should be between 0 and 1')
        
        if self.MAX_PROCESSING_TIME <= 0:
            validation_results['valid'] = False
            validation_results['errors'].append('MAX_PROCESSING_TIME must be positive')
        
        if self.SESSION_TIMEOUT <= 0:
            validation_results['valid'] = False
            validation_results['errors'].append('SESSION_TIMEOUT must be positive')
        
        # Validate challenge length limits
        if self.MIN_CHALLENGE_LENGTH >= self.MAX_CHALLENGE_LENGTH:
            validation_results['valid'] = False
            validation_results['errors'].append('MIN_CHALLENGE_LENGTH must be less than MAX_CHALLENGE_LENGTH')
        
        # Validate RFT base parameters
        rft_params = self.get_rft_base_parameters()
        for param_name, param_value in rft_params.items():
            if param_value <= 0:
                validation_results['warnings'].append(f'{param_name.upper()} should be positive')
        
        # Validate threading settings
        if self.ENABLE_THREADING and self.MAX_WORKER_THREADS <= 0:
            validation_results['valid'] = False
            validation_results['errors'].append('MAX_WORKER_THREADS must be positive when threading is enabled')
        
        # Validate rate limiting
        if self.RATE_LIMIT_ENABLED:
            if self.RATE_LIMIT_REQUESTS <= 0:
                validation_results['valid'] = False
                validation_results['errors'].append('RATE_LIMIT_REQUESTS must be positive')
            
            if self.RATE_LIMIT_WINDOW <= 0:
                validation_results['valid'] = False
                validation_results['errors'].append('RATE_LIMIT_WINDOW must be positive')
        
        return validation_results
    
    def get_debug_info(self) -> Dict[str, Any]:
        """Get configuration debug information"""
        
        return {
            'bot_info': {
                'name': self.BOT_NAME,
                'version': self.BOT_VERSION,
                'description': self.BOT_DESCRIPTION
            },
            'rft_parameters': self.get_rft_base_parameters(),
            'calculation_limits': self.get_calculation_limits(),
            'session_settings': {
                'timeout': self.SESSION_TIMEOUT,
                'max_concurrent': self.MAX_CONCURRENT_SESSIONS,
                'cleanup_interval': self.SESSION_CLEANUP_INTERVAL
            },
            'challenge_settings': {
                'min_length': self.MIN_CHALLENGE_LENGTH,
                'max_length': self.MAX_CHALLENGE_LENGTH,
                'max_processing_time': self.MAX_PROCESSING_TIME
            },
            'feature_flags': {
                'debug_mode': self.DEBUG_MODE,
                'verbose_logging': self.VERBOSE_LOGGING,
                'enable_metrics': self.ENABLE_METRICS,
                'adaptive_parameters': self.ENABLE_ADAPTIVE_PARAMETERS,
                'experimental_features': self.ENABLE_EXPERIMENTAL_FEATURES
            }
        }
    
    def update_parameter(self, parameter_name: str, parameter_value: Any) -> bool:
        """Update a configuration parameter dynamically"""
        
        if hasattr(self, parameter_name):
            # Type validation based on current parameter type
            current_value = getattr(self, parameter_name)
            
            try:
                # Convert to appropriate type
                if isinstance(current_value, bool):
                    if isinstance(parameter_value, str):
                        parameter_value = parameter_value.lower() == 'true'
                elif isinstance(current_value, int):
                    parameter_value = int(parameter_value)
                elif isinstance(current_value, float):
                    parameter_value = float(parameter_value)
                
                setattr(self, parameter_name, parameter_value)
                return True
                
            except (ValueError, TypeError):
                return False
        
        return False
    
    def export_config(self) -> Dict[str, Any]:
        """Export current configuration as dictionary"""
        
        config_dict = {}
        
        for attr_name in dir(self):
            if not attr_name.startswith('_') and not callable(getattr(self, attr_name)):
                attr_value = getattr(self, attr_name)
                
                # Only include basic types
                if isinstance(attr_value, (str, int, float, bool, dict, list)):
                    config_dict[attr_name] = attr_value
        
        return config_dict
