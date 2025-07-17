#!/usr/bin/env python3
"""
EV Charging Data Warehouse - Environment Test Script
Tests all required packages and configurations for the project.
"""

import sys
import platform
from datetime import datetime

def test_environment():
    """Test all required packages and environment setup."""
    
    print("=" * 60)
    print("🔋 EV Charging Data Warehouse - Environment Test")
    print("=" * 60)
    print(f"📅 Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python Version: {sys.version}")
    print(f"💻 Platform: {platform.system()} {platform.release()}")
    print(f"📁 Virtual Environment: {'✅ Active' if hasattr(sys, 'real_prefix') or sys.base_prefix != sys.prefix else '❌ Not Active'}")
    print()
    
    # Test packages
    packages_to_test = [
        # Core Data Processing
        ("pandas", "Data manipulation and analysis"),
        ("numpy", "Numerical computing"),
        ("sqlalchemy", "Database toolkit"),
        
        # Snowflake Integration
        ("snowflake.connector", "Snowflake database connectivity"),
        ("snowflake.sqlalchemy", "Snowflake SQLAlchemy dialect"),
        
        # ETL & Pipeline
        ("requests", "HTTP library for API calls"),
        ("dotenv", "Environment variable management"),
        
        # Analytics & Visualization
        ("streamlit", "Web dashboard framework"),
        ("plotly", "Interactive visualizations"),
        ("matplotlib", "Static plotting library"),
        ("seaborn", "Statistical visualizations"),
        
        # Weather Data
        ("pyowm", "Weather API integration"),
        
        # Data Validation
        ("great_expectations", "Data quality framework"),
        
        # Testing & Development
        ("pytest", "Testing framework"),
        ("jupyter", "Interactive notebooks"),
        ("IPython", "Enhanced Python shell"),
        
        # Utilities
        ("faker", "Synthetic data generation"),
        ("pytz", "Timezone handling"),
    ]
    
    print("📦 Package Import Tests:")
    print("-" * 40)
    
    failed_imports = []
    
    for package, description in packages_to_test:
        try:
            __import__(package)
            print(f"✅ {package:<25} - {description}")
        except ImportError as e:
            print(f"❌ {package:<25} - FAILED: {str(e)}")
            failed_imports.append(package)
    
    print()
    print("🔍 Package Version Check:")
    print("-" * 40)
    
    version_checks = [
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("streamlit", "streamlit"),
        ("plotly", "plotly"),
        ("matplotlib", "matplotlib"),
        ("pytest", "pytest"),
    ]
    
    for package_name, import_name in version_checks:
        try:
            module = __import__(import_name)
            version = getattr(module, '__version__', 'Version not available')
            print(f"📊 {package_name:<15} - Version: {version}")
        except ImportError:
            print(f"❌ {package_name:<15} - Not installed")
    
    print()
    print("🛠️  Environment Summary:")
    print("-" * 40)
    
    if not failed_imports:
        print("✅ All packages imported successfully!")
        print("✅ Environment is ready for EV Charging Data Warehouse development")
        print("✅ You can proceed to Task 3: Register Free Accounts")
    else:
        print(f"❌ {len(failed_imports)} packages failed to import:")
        for package in failed_imports:
            print(f"   - {package}")
        print("❌ Please reinstall missing packages before proceeding")
    
    print("=" * 60)
    return len(failed_imports) == 0

if __name__ == "__main__":
    success = test_environment()
    sys.exit(0 if success else 1)
