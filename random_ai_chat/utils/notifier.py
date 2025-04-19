from streamlit.runtime import Runtime
from streamlit.runtime.app_session import AppSession

def get_streamlit_sessions() -> list[AppSession]:
    runtime: Runtime = Runtime.instance()
    return [s.session for s in runtime._session_mgr.list_sessions()]

def notify() -> None:
    for session in get_streamlit_sessions():
        session._handle_rerun_script_request()