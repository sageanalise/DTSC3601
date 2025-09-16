import shlex
import os
from pathlib import Path
import modal

streamlit_script_local_path = Path(__file__).parent / "streamlit_run.py"
streamlit_script_remote_path = "/root/streamlit_run.py"

image = (
    modal.Image.debian_slim(python_version="3.9")
    .pip_install("streamlit", "supabase", "pandas", "plotly")
    .add_local_file(streamlit_script_local_path, streamlit_script_remote_path)
)

app = modal.App(name="usage-dashboard", image=image)

@app.function()
@modal.web_server(8000)
def run():
    target = shlex.quote(streamlit_script_remote_path)
    cmd = f"streamlit run {target} --server.port 8000 --server.enableCORS=false --server.enableXsrfProtection=false"

    env_vars = {
        "SUPABASE_KEY": os.getenv("SUPABASE_KEY"),
        "SUPABASE_URL": os.getenv("SUPABASE_URL"),
    }

    os.execle("/bin/bash", "bash", "-c", cmd, env_vars)