from prefect_flows.template_flow import hello_world


def main() -> None:
    hello_world.serve(name="kohls t r b deployment")
