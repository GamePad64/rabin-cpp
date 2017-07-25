from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="gamepad64", channel="stable")
    builder.add_common_builds()
    builder.run()
