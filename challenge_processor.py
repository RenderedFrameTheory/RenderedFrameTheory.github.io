"""
Challenge Processor - Parses and categorizes user challenges for RFT processing
Analyzes semantic content, complexity, and challenge characteristics
"""

import re
import math
import logging
from typing import Dict, List, Tuple, Any
from datetime import datetime
import numpy as np

logger = logging.getLogger(__name__)

class ChallengeProcessor:
    """
    Processes and analyzes user challenges for RFT engine processing
    Categorizes challenge types and calculates semantic properties
    """
    
    def __init__(self):
        """Initialize challenge processor with analysis parameters"""
        
        # Challenge type keywords and their weights
        self.challenge_keywords = {
            'cognitive': ['consciousness', 'mind', 'thinking', 'cognitive', 'awareness', 'perception', 'brain'],
            'theoretical': ['theory', 'hypothesis', 'model', 'framework', 'principle', 'law', 'equation'],
            'quantum': ['quantum', 'entanglement', 'superposition', 'wave', 'particle', 'measurement', 'collapse'],
            'temporal': ['time', 'temporal', 'causality', 'chronology', 'sequence', 'duration', 'timing'],
            'perceptual': ['perceive', 'observe', 'see', 'hear', 'sense', 'experience', 'feel', 'sensation'],
            'consciousness': ['conscious', 'unconscious', 'awareness', 'subjective', 'experience', 'qualia'],
            'observer': ['observer', 'observation', 'observe', 'witness', 'viewpoint', 'perspective'],
            'reality': ['reality', 'existence', 'being', 'ontology', 'actual', 'real', 'manifest'],
            'synchronization': ['sync', 'synchronize', 'align', 'coordinate', 'harmony', 'resonance'],
            'ai_alignment': ['artificial', 'intelligence', 'ai', 'machine', 'algorithm', 'neural', 'learning']
        }
        
        # Complexity indicators
        self.complexity_indicators = {
            'high': ['multi-dimensional', 'paradox', 'infinite', 'recursive', 'non-linear', 'chaotic'],
            'medium': ['relationship', 'interaction', 'correlation', 'influence', 'connection', 'dynamic'],
            'low': ['basic', 'simple', 'direct', 'linear', 'straightforward', 'elementary']
        }
        
        # Scientific discipline keywords
        self.discipline_keywords = {
            'physics': ['physics', 'force', 'energy', 'matter', 'field', 'particle', 'wave'],
            'neuroscience': ['neuron', 'brain', 'neural', 'synaptic', 'cortex', 'consciousness'],
            'psychology': ['psychology', 'behavior', 'mental', 'cognitive', 'emotional', 'perception'],
            'philosophy': ['philosophy', 'metaphysics', 'ontology', 'epistemology', 'ethics', 'logic'],
            'mathematics': ['mathematics', 'equation', 'function', 'variable', 'calculation', 'proof'],
            'computer_science': ['computer', 'algorithm', 'data', 'information', 'computation', 'artificial']
        }
        
        logger.info("Challenge Processor initialized with keyword analysis capabilities")
    
    def process_challenge(self, challenge_text: str, user_id: int) -> Dict[str, Any]:
        """
        Process and analyze a user challenge
        
        Args:
            challenge_text: The challenge text to analyze
            user_id: User identifier for context
            
        Returns:
            Dictionary containing challenge analysis results
        """
        
        # Clean and normalize text
        normalized_text = self._normalize_text(challenge_text)
        
        # Analyze challenge type
        challenge_type = self._analyze_challenge_type(normalized_text)
        
        # Calculate complexity
        complexity = self._calculate_complexity(normalized_text)
        
        # Calculate semantic density
        semantic_density = self._calculate_semantic_density(normalized_text)
        
        # Determine scientific discipline
        discipline = self._determine_discipline(normalized_text)
        
        # Calculate entropy
        entropy = self._calculate_text_entropy(normalized_text)
        
        # Analyze question structure
        question_structure = self._analyze_question_structure(normalized_text)
        
        # Calculate urgency based on language patterns
        urgency = self._calculate_urgency(normalized_text)
        
        # Extract key concepts
        key_concepts = self._extract_key_concepts(normalized_text)
        
        # Analyze observer focus
        observer_focus = self._analyze_observer_focus(normalized_text)
        
        challenge_data = {
            'original_text': challenge_text,
            'normalized_text': normalized_text,
            'user_id': user_id,
            'type': challenge_type,
            'complexity': complexity,
            'semantic_density': semantic_density,
            'discipline': discipline,
            'entropy': entropy,
            'question_structure': question_structure,
            'urgency': urgency,
            'key_concepts': key_concepts,
            'observer_focus': observer_focus,
            'word_count': len(normalized_text.split()),
            'processing_timestamp': datetime.now().isoformat()
        }
        
        # SignalScan – Interference Detector
        interference_detected = self._detect_signal_interference(normalized_text, user_id, semantic_density)
        challenge_data['interference_detected'] = interference_detected
        
        # Guardian_Ω – Theft Pattern Watchdog  
        theft_alert = self._guardian_omega_scan(normalized_text, user_id)
        challenge_data['theft_alert'] = theft_alert
        
        logger.info(f"Challenge processed: Type={challenge_type}, Complexity={complexity:.2f}, Density={semantic_density:.2f}")
        
        return challenge_data
    
    def _normalize_text(self, text: str) -> str:
        """Normalize text for analysis"""
        
        # Convert to lowercase
        normalized = text.lower()
        
        # Remove extra whitespace
        normalized = re.sub(r'\s+', ' ', normalized)
        
        # Remove special characters but keep basic punctuation
        normalized = re.sub(r'[^\w\s\?\!\.\,\;\:]', '', normalized)
        
        # Strip leading/trailing whitespace
        normalized = normalized.strip()
        
        return normalized
    
    def _analyze_challenge_type(self, text: str) -> str:
        """Analyze and categorize the challenge type"""
        
        type_scores = {}
        words = text.split()
        
        # Calculate scores for each challenge type
        for challenge_type, keywords in self.challenge_keywords.items():
            score = 0
            for keyword in keywords:
                # Count exact matches
                score += text.count(keyword)
                
                # Count partial matches (for compound words)
                for word in words:
                    if keyword in word and len(word) > len(keyword):
                        score += 0.5
            
            type_scores[challenge_type] = score
        
        # Find the type with highest score
        if type_scores:
            primary_type = max(type_scores, key=type_scores.get)
            
            # Only return a specific type if the score is above threshold
            if type_scores[primary_type] > 0:
                return primary_type
        
        return 'general'
    
    def _calculate_complexity(self, text: str) -> float:
        """Calculate challenge complexity score (0.0 to 1.0)"""
        
        complexity_score = 0.0
        
        # Check for complexity indicators
        for level, indicators in self.complexity_indicators.items():
            for indicator in indicators:
                if indicator in text:
                    if level == 'high':
                        complexity_score += 0.3
                    elif level == 'medium':
                        complexity_score += 0.2
                    elif level == 'low':
                        complexity_score -= 0.1
        
        # Analyze sentence structure complexity
        sentences = text.split('.')
        avg_sentence_length = np.mean([len(s.split()) for s in sentences if s.strip()])
        
        # Longer sentences typically indicate higher complexity
        length_complexity = min(avg_sentence_length / 20, 0.5)
        complexity_score += length_complexity
        
        # Check for question complexity
        question_count = text.count('?')
        nested_questions = text.count('how') + text.count('why') + text.count('what if')
        
        question_complexity = min((question_count + nested_questions) * 0.1, 0.3)
        complexity_score += question_complexity
        
        # Check for scientific/technical terms
        technical_patterns = [
            r'\b\w+tion\b',  # -tion endings
            r'\b\w+ism\b',   # -ism endings
            r'\b\w+ology\b', # -ology endings
            r'\b\w+metric\b' # -metric endings
        ]
        
        technical_score = 0
        for pattern in technical_patterns:
            matches = len(re.findall(pattern, text))
            technical_score += matches * 0.05
        
        complexity_score += min(technical_score, 0.3)
        
        # Normalize to 0.0-1.0 range
        return max(0.0, min(complexity_score, 1.0))
    
    def _calculate_semantic_density(self, text: str) -> float:
        """Calculate semantic density of the challenge text"""
        
        words = text.split()
        word_count = len(words)
        
        if word_count == 0:
            return 0.0
        
        # Count unique meaningful words (excluding common stop words)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 
                     'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 
                     'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
                     'will', 'would', 'could', 'should', 'may', 'might', 'can',
                     'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she',
                     'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'}
        
        meaningful_words = [word for word in words if word not in stop_words and len(word) > 2]
        unique_meaningful_words = set(meaningful_words)
        
        # Calculate basic density
        basic_density = len(unique_meaningful_words) / word_count
        
        # Bonus for scientific/technical vocabulary
        scientific_word_count = 0
        for category_keywords in self.challenge_keywords.values():
            for keyword in category_keywords:
                scientific_word_count += text.count(keyword)
        
        scientific_bonus = min(scientific_word_count / word_count, 0.3)
        
        semantic_density = basic_density + scientific_bonus
        
        return max(0.0, min(semantic_density, 1.0))
    
    def _determine_discipline(self, text: str) -> str:
        """Determine the primary scientific discipline"""
        
        discipline_scores = {}
        
        for discipline, keywords in self.discipline_keywords.items():
            score = 0
            for keyword in keywords:
                score += text.count(keyword)
            discipline_scores[discipline] = score
        
        if discipline_scores:
            primary_discipline = max(discipline_scores, key=discipline_scores.get)
            if discipline_scores[primary_discipline] > 0:
                return primary_discipline
        
        return 'interdisciplinary'
    
    def _calculate_text_entropy(self, text: str) -> float:
        """Calculate information entropy of the text"""
        
        if not text:
            return 0.0
        
        # Count character frequencies
        char_counts = {}
        for char in text:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        # Calculate entropy
        text_length = len(text)
        entropy = 0.0
        
        for count in char_counts.values():
            probability = count / text_length
            if probability > 0:
                entropy -= probability * math.log2(probability)
        
        # Normalize entropy (English text typically has entropy around 4.5)
        normalized_entropy = min(entropy / 4.5, 1.0)
        
        return normalized_entropy
    
    def _analyze_question_structure(self, text: str) -> Dict[str, Any]:
        """Analyze the structure of the question/challenge"""
        
        structure = {
            'is_question': '?' in text,
            'question_words': [],
            'has_hypothesis': False,
            'has_conditions': False,
            'has_examples': False
        }
        
        # Identify question words
        question_words = ['what', 'how', 'why', 'when', 'where', 'who', 'which', 'can', 'does', 'is']
        for word in question_words:
            if word in text:
                structure['question_words'].append(word)
        
        # Check for hypothesis indicators
        hypothesis_indicators = ['if', 'suppose', 'assume', 'given that', 'hypothetically']
        structure['has_hypothesis'] = any(indicator in text for indicator in hypothesis_indicators)
        
        # Check for conditional statements
        conditional_indicators = ['when', 'if', 'unless', 'provided that', 'in case']
        structure['has_conditions'] = any(indicator in text for indicator in conditional_indicators)
        
        # Check for examples
        example_indicators = ['example', 'instance', 'such as', 'like', 'for example']
        structure['has_examples'] = any(indicator in text for indicator in example_indicators)
        
        return structure
    
    def _calculate_urgency(self, text: str) -> float:
        """Calculate challenge urgency based on language patterns"""
        
        urgency_score = 0.5  # Base urgency
        
        # High urgency indicators
        high_urgency_words = ['urgent', 'immediate', 'critical', 'emergency', 'now', 'quickly']
        for word in high_urgency_words:
            if word in text:
                urgency_score += 0.2
        
        # Low urgency indicators
        low_urgency_words = ['eventually', 'someday', 'general', 'broadly', 'theoretically']
        for word in low_urgency_words:
            if word in text:
                urgency_score -= 0.1
        
        # Question marks can indicate higher urgency
        question_marks = text.count('?')
        urgency_score += min(question_marks * 0.1, 0.2)
        
        # Exclamation marks indicate higher urgency
        exclamations = text.count('!')
        urgency_score += min(exclamations * 0.15, 0.3)
        
        return max(0.0, min(urgency_score, 1.0))
    
    def _extract_key_concepts(self, text: str) -> List[str]:
        """Extract key concepts from the challenge text"""
        
        key_concepts = []
        words = text.split()
        
        # Extract multi-word scientific terms
        scientific_terms = []
        for i in range(len(words) - 1):
            two_word_term = f"{words[i]} {words[i+1]}"
            
            # Check if it's a scientific term
            is_scientific = False
            for category_keywords in self.challenge_keywords.values():
                if any(keyword in two_word_term for keyword in category_keywords):
                    is_scientific = True
                    break
            
            if is_scientific:
                scientific_terms.append(two_word_term)
        
        key_concepts.extend(scientific_terms)
        
        # Extract single important words
        important_single_words = []
        for word in words:
            if len(word) > 4:  # Focus on longer words
                is_important = False
                for category_keywords in self.challenge_keywords.values():
                    if word in category_keywords:
                        is_important = True
                        break
                
                if is_important:
                    important_single_words.append(word)
        
        key_concepts.extend(important_single_words)
        
        # Remove duplicates and return top concepts
        unique_concepts = list(set(key_concepts))
        return unique_concepts[:10]  # Return top 10 concepts
    
    def _detect_signal_interference(self, text: str, user_id: int, semantic_density: float) -> Dict[str, Any]:
        """
        SignalScan – Interference Detector
        Detects unusual Δφ spikes and simulation interference
        """
        
        interference_result = {
            'detected': False,
            'spike_level': 0.0,
            'warning_message': None
        }
        
        try:
            # Load observer log to check for Δφ patterns
            log_file = 'logs/observer_log.json'
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    log_data = json.load(f)
                
                # Get user's recent Δφ values
                user_entries = [entry for entry in log_data if entry['user_id'] == user_id]
                
                if len(user_entries) >= 3:
                    delta_phi_values = [entry['delta_phi'] for entry in user_entries[-10:]]
                    mean_delta_phi = sum(delta_phi_values) / len(delta_phi_values)
                    
                    # Check current semantic density for spike
                    current_spike = semantic_density * 3.14159  # Convert to pseudo-Δφ
                    
                    # Detect interference if spike > 3× mean
                    if current_spike > 3 * mean_delta_phi and mean_delta_phi > 0:
                        interference_result['detected'] = True
                        interference_result['spike_level'] = current_spike / mean_delta_phi
                        interference_result['warning_message'] = "⚠️ Simulation interference detected in your challenge. Render delay exceeds norm."
                        
                        # Log interference
                        self._log_interference(user_id, text, interference_result)
            
        except Exception as e:
            logger.error(f"Error in signal interference detection: {str(e)}")
        
        return interference_result
    
    def _guardian_omega_scan(self, text: str, user_id: int) -> Dict[str, Any]:
        """
        Guardian_Ω – Theft Pattern Watchdog
        Scans for unauthorized use of RFT equation formats
        """
        
        theft_result = {
            'alert_triggered': False,
            'equation_matches': [],
            'risk_level': 'LOW'
        }
        
        try:
            # Define known RFT equation patterns
            rft_equation_patterns = [
                r'Ω\s*=\s*\(.*Ω_obs.*χ_Liam.*\)\s*/\s*\(.*Δφ.*Υ.*\)',
                r'omega\s*=\s*\(.*omega_obs.*chi_liam.*\)\s*/\s*\(.*delta_phi.*upsilon.*\)',
                r'τ_eff\s*=.*observer.*timing',
                r'Δφ\s*/\s*τ_eff\s*=\s*Ω_obs'
            ]
            
            # Known contributor patterns (placeholder - would be actual IDs in production)
            known_contributors = {
                12345: 'authorized_rft_researcher',  # Replace with actual user IDs
                67890: 'rft_team_member'
            }
            
            found_equations = []
            for pattern in rft_equation_patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                if matches:
                    found_equations.extend(matches)
            
            if found_equations and user_id not in known_contributors:
                theft_result['alert_triggered'] = True
                theft_result['equation_matches'] = found_equations
                theft_result['risk_level'] = 'HIGH' if len(found_equations) > 1 else 'MEDIUM'
                
                # Log theft flag (passive - doesn't affect user experience)
                self._log_theft_flag(user_id, text, theft_result)
                
                logger.warning(f"Guardian_Ω Alert: Unmatched equation source from user {user_id}")
            
        except Exception as e:
            logger.error(f"Error in Guardian_Ω scan: {str(e)}")
        
        return theft_result
    
    def _log_interference(self, user_id: int, text: str, interference_data: Dict[str, Any]):
        """Log interference detection to JSON file"""
        
        log_file = 'logs/interference_log.json'
        
        try:
            # Load existing log
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    log_data = json.load(f)
            else:
                log_data = []
            
            # Create log entry
            entry = {
                'timestamp': datetime.now().isoformat(),
                'user_id': user_id,
                'challenge_text': text[:200] + '...' if len(text) > 200 else text,
                'spike_level': interference_data['spike_level'],
                'warning_issued': interference_data['detected']
            }
            
            log_data.append(entry)
            
            # Keep only last 1000 entries
            if len(log_data) > 1000:
                log_data = log_data[-1000:]
            
            # Save log
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            logger.error(f"Failed to log interference: {str(e)}")
    
    def _log_theft_flag(self, user_id: int, text: str, theft_data: Dict[str, Any]):
        """Log theft pattern detection to JSON file"""
        
        log_file = 'logs/theft_flags.json'
        
        try:
            # Load existing log
            if os.path.exists(log_file):
                with open(log_file, 'r', encoding='utf-8') as f:
                    log_data = json.load(f)
            else:
                log_data = []
            
            # Create log entry
            entry = {
                'timestamp': datetime.now().isoformat(),
                'user_id': user_id,
                'challenge_text': text[:200] + '...' if len(text) > 200 else text,
                'equation_matches': theft_data['equation_matches'],
                'risk_level': theft_data['risk_level'],
                'alert_triggered': theft_data['alert_triggered']
            }
            
            log_data.append(entry)
            
            # Keep only last 500 entries
            if len(log_data) > 500:
                log_data = log_data[-500:]
            
            # Save log
            with open(log_file, 'w', encoding='utf-8') as f:
                json.dump(log_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            logger.error(f"Failed to log theft flag: {str(e)}")
    
    def _analyze_observer_focus(self, text: str) -> Dict[str, float]:
        """Analyze the observer focus aspects of the challenge"""
        
        observer_aspects = {
            'self_reference': 0.0,
            'external_observation': 0.0,
            'meta_cognitive': 0.0,
            'consciousness_focus': 0.0
        }
        
        # Self-reference indicators
        self_ref_words = ['i', 'me', 'my', 'myself', 'personal', 'subjective']
        for word in self_ref_words:
            if word in text:
                observer_aspects['self_reference'] += 0.2
        
        # External observation indicators
        external_obs_words = ['observe', 'measure', 'detect', 'monitor', 'witness', 'perceive']
        for word in external_obs_words:
            if word in text:
                observer_aspects['external_observation'] += 0.2
        
        # Meta-cognitive indicators
        meta_cog_words = ['thinking about thinking', 'awareness of', 'conscious of', 'meta']
        for phrase in meta_cog_words:
            if phrase in text:
                observer_aspects['meta_cognitive'] += 0.3
        
        # Consciousness focus indicators
        consciousness_words = ['consciousness', 'awareness', 'experience', 'subjective', 'qualia']
        for word in consciousness_words:
            if word in text:
                observer_aspects['consciousness_focus'] += 0.2
        
        # Normalize values to 0.0-1.0 range
        for aspect in observer_aspects:
            observer_aspects[aspect] = min(observer_aspects[aspect], 1.0)
        
        return observer_aspects
    
    def get_challenge_statistics(self) -> Dict[str, Any]:
        """Get statistics about processed challenges"""
        
        # This would be enhanced with actual tracking in a production system
        return {
            'total_processed': 0,
            'type_distribution': {},
            'average_complexity': 0.0,
            'common_concepts': []
        }
