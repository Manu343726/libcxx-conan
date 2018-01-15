from conans.model.conan_file import ConanFile
from conans import CMake
import os

############### CONFIGURE THESE VALUES ##################
default_user = "smspillaz"
default_channel = "stable"
#########################################################

channel = os.getenv("CONAN_CHANNEL", default_channel)
username = os.getenv("CONAN_USERNAME", default_user)


class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "compiler", "arch", "build_type"
    requires = ("llvm/3.8.0@%s/%s" % (username, channel),
                "libcxx/3.8.0@%s/%s" % (username, channel))
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        pass
