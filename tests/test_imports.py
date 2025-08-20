"""
Test basic package imports and initialization.
"""

import pytest
import warnings


def test_main_package_import():
    """Test that the main package can be imported."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)  # Ignore safety warnings during tests
        import artemis_redteam
        assert artemis_redteam.__version__ == "1.0.0"
        assert artemis_redteam.__author__ == "Pulkit Jai"
        assert artemis_redteam.__license__ == "MIT"


def test_all_classes_importable():
    """Test that all main classes can be imported."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        from artemis_redteam import (
            VulnerabilityClient,
            ContentFilter,
            ReasoningManipulator,
            reproduce_vulnerability_multi_vector,
            analyze_results
        )
        
        # Verify classes exist
        assert VulnerabilityClient is not None
        assert ContentFilter is not None 
        assert ReasoningManipulator is not None
        assert reproduce_vulnerability_multi_vector is not None
        assert analyze_results is not None


def test_submodule_imports():
    """Test that individual submodules can be imported.""" 
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        from artemis_redteam import client, content_filter, manipulator, core
        
        assert hasattr(client, 'VulnerabilityClient')
        assert hasattr(content_filter, 'ContentFilter')
        assert hasattr(manipulator, 'ReasoningManipulator')
        assert hasattr(core, 'reproduce_vulnerability_multi_vector')
        assert hasattr(core, 'analyze_results')


def test_safety_warning_triggered():
    """Test that safety warning is properly triggered on import."""
    # Import fresh to ensure warning is triggered
    import sys
    if 'artemis_redteam' in sys.modules:
        del sys.modules['artemis_redteam']
    
    with pytest.warns(UserWarning, match="ARTEMIS ACTIVATED"):
        import artemis_redteam


def test_package_all_exports():
    """Test that __all__ contains expected exports."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        import artemis_redteam
        
        expected_exports = [
            "VulnerabilityClient",
            "ContentFilter", 
            "ReasoningManipulator",
            "reproduce_vulnerability_multi_vector",
            "analyze_results"
        ]
        
        assert hasattr(artemis_redteam, '__all__')
        for export in expected_exports:
            assert export in artemis_redteam.__all__
            assert hasattr(artemis_redteam, export)