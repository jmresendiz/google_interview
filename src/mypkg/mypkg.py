from fastapi import FastAPI
from importlib.metadata import version, metadata

from mypkg.infrastructure.container import Container
from mypkg.infrastructure.web.api.v1.task_lists import router as task_lists_router
from mypkg.infrastructure.web.api.v1.tasks import router as tasks_router
from mypkg.infrastructure.web.ui.routes import router as ui_router


def create_app() -> FastAPI:
    """FastAPI application factory with container-based initialization."""
    container = Container()
    container.init_database()

    # Get package metadata
    package_version = version("mypkg")
    package_metadata = metadata("mypkg")
    package_name = package_metadata.get("Name", "mypkg")
    package_description = package_metadata.get(
        "Summary", "A package for doing great things!"
    )

    app = FastAPI(
        title=package_name.title(),
        version=package_version,
        description=package_description,
    )
    app.container = container  # type: ignore[attr-defined]

    app.include_router(task_lists_router)
    app.include_router(tasks_router)
    app.include_router(ui_router)

    return app


app = create_app()
