[build-system]
requires = [
  "setuptools>=60",
]

[project]
name = "${project_name}"

version = "0.1.0"
description = "A ${kind} plugin for anemoi.${package}"
readme = { text = "A ${kind} plugin for anemoi.${package}", content-type = "text/markdown" }

keywords = [
  "${kind}",
  "${package}",
  "ai",
  "tools",
]

license = { text = "Apache License Version 2.0" }
authors = [
  { name = "John Doe", email = "author@example.com" },
]
requires-python = ">=3.10"
classifiers = [
  "Development Status :: 3 - Alpha",
  "Operating System :: OS Independent",
  "Programming Language :: Python :: 3 :: Only",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: 3.12",
  "Programming Language :: Python :: 3.13",
  "Programming Language :: Python :: Implementation :: CPython",
  "Programming Language :: Python :: Implementation :: PyPy",
]

urls.Homepage = "https://github.com/ecmwf/anemoi-plugins"

entry-points."${entry_point}".${name} = "${plugin_package}.${name}:${plugin_class}"
