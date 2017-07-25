from conans import ConanFile, CMake, tools


class RabincppConan(ConanFile):
    name = "rabin-cpp"
    version = "1.0"
    license = "Simplified BSD License"
    url = "https://github.com/gamepad64/rabin-cpp"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "ext_boost": [False, True]}
    default_options = "shared=False\next_boost=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/gamepad64/rabin-cpp.git")
        self.run("cd rabin-cpp && git checkout 1.0")
        
    def requirements(self):
        if not self.options.ext_boost:
            self.requires.add("Boost/1.62.0@lasote/stable", private=False)

    def build(self):
        cmake = CMake(self)
        self.run('cmake rabin-cpp %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="rabin-cpp")
        self.copy("*rabin-cpp.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rabin-cpp"]
