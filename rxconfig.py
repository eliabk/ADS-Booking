import reflex as rx

config = rx.Config(
    app_name="ads_booking_python",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)