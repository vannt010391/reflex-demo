import reflex as rx


class WebuiConfig(rx.Config):
    pass


config = WebuiConfig(
    app_name="webui",
    api_url="https://reflex-chat-m7fa.onrender.com",
    # env=rx.Env.DEV,
    # frontend_packages=[
    #     "react-loading-icons",
    # ],
)
