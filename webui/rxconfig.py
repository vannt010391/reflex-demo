import reflex as rx


class WebuiConfig(rx.Config):
    pass


config = WebuiConfig(
    app_name="webui",
    api_url="http://reflex-chat-m7fa.onrender.com:8000",
    # env=rx.Env.DEV,
    # frontend_packages=[
    #     "react-loading-icons",
    # ],
)
