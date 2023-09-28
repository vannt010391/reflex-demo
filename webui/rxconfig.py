import reflex as rx


class WebuiConfig(rx.Config):
    pass


config = WebuiConfig(
    app_name="webui",
    db_url="sqlite:///reflex.db",
    # api_url="https://reflex-demo.onrender.com:8000",
    # env=rx.Env.DEV,
    # frontend_packages=[
    #     "react-loading-icons",
    # ],
)
