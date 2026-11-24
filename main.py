"""Drop one daft kitchen-gadget pitch, a single sentence, into the entry file."""

from pathlib import Path

TOASTER_PITCH = "My toaster launches every slice on a tiny parachute, so no toast ever lands butter-side down again."
DESTINATION = Path("/output/entry.txt")


def publish_pitch() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(TOASTER_PITCH, encoding="utf-8")


if __name__ == "__main__":
    publish_pitch()
