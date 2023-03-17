import dismake, config
from dismake.interaction import Interaction


app = dismake.Bot(
    token=config.token,
    client_public_key=config.public_key,
    client_id=config.client_id,
    route="/",
)


@app.on_event("startup")
async def on_startup():
    return


@app.command(
    name="echo",
    description="Echo",
    options=[
        dismake.Option(name="text", description="Say something.", required=True),
    ],
)
async def alive(interaction: Interaction):
    await interaction.respond(
        f"**You Said**: \n{interaction.data.options[0].value}"  # type: ignore
    )


if __name__ == "__main__":
    app.run(app=f"main:app", reload=True)
