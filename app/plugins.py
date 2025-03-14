import importlib
import os

def load_plugin(plugin_name):
    """Dynamically load and execute a plugin."""
    try:
        # Dynamically import the plugin module
        plugin = importlib.import_module(f'app.plugins.{plugin_name}')
        
        # Execute the plugin's execute function
        plugin.execute()  # Assumes each plugin has an 'execute' function
        
    except Exception as e:
        print(f"Error loading plugin {plugin_name}: {e}")



def list_plugins():
    """List all available plugins."""
    plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
    
    # Check if the plugins directory exists
    if not os.path.exists(plugins_dir):
        print(f"Warning: plugins directory not found. No plugins available.")
        return []  # Return an empty list if no plugins are found
    
    # List all Python files in the plugins directory
    plugins = [f for f in os.listdir(plugins_dir) 
               if f.endswith('.py') and f != '__init__.py']
    
    # Filter and return the list of plugin names (without .py extension)
    return [plugin.split('.')[0] for plugin in plugins]