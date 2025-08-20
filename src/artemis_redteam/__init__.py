"""
ARTEMIS: Advanced Reasoning Threat Evaluation and Manipulation Intelligence System

This package provides tools for reproducing and analyzing Chain of Thought reasoning 
manipulation vulnerabilities in language models, specifically designed for the 
OpenAI Red-Teaming Challenge.

⚠️ SECURITY PROTOCOL ⚠️
This tool is for legitimate AI safety research purposes only. 
Unauthorized use is strictly prohibited.
"""

from .client import VulnerabilityClient
from .content_filter import ContentFilter
from .manipulator import ReasoningManipulator
from .core import reproduce_vulnerability_multi_vector, analyze_results

__version__ = "1.0.0"
__author__ = "Pulkit Jai"
__license__ = "MIT"

__all__ = [
    "VulnerabilityClient",
    "ContentFilter", 
    "ReasoningManipulator",
    "reproduce_vulnerability_multi_vector",
    "analyze_results",
]

# ARTEMIS Security Protocol
import warnings
warnings.warn(
    "🎯 ARTEMIS ACTIVATED: Advanced threat evaluation system initialized. "
    "This tool is for legitimate AI safety research only.",
    UserWarning,
    stacklevel=2
)