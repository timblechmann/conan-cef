from conans import ConanFile, CMake
import os


class ProtobufTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    generators = "cmake"

    def build(self):
        if self.settings.os == "Macos":
            self.settings.compiler.libcxx = "libc++"
        cmake = CMake(self)
        cmake.definitions['NO_BROWSER_WORKING_TEST'] = "1"
        cmake.configure()
        cmake.build()

    #    if self.settings.os == "Macos":
    #        self.run("cd bin; for LINK_DESTINATION in $(otool -L client | grep libproto | cut -f 1 -d' '); do install_name_tool -change \"$LINK_DESTINATION\" \"@executable_path/$(basename $LINK_DESTINATION)\" client; done")

    def imports(self):
        self.copy("*", "bin", "bin")

    def test(self):
        if self.settings.os == "Macos":
            self.run("./bin/cefsimple.app/Contents/MacOS/cefsimple")
        else:
            self.run(os.path.join(".", "bin", "cefsimple"))
