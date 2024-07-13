# ArgusDash Template Plugin

Download or use this template repository as a reference while developing a plugin for ArgusDash.

## Special directories

 - `backend`: This directory hold all the python files of the plugin. While plugins do not have to have extensive backend code, they do have to expose the frontend functionalities by using the API provided. The only file that has to exist is `main.py` that has an `init` function returning an instance of an implementation of the abstract `Plugin` class. To import submodules from this directory into your `main.py` and other source files, use the path `plugins.plugins.{plugin_name}.backend`.
 - `frontend`: This directory contains all the `.svelte` widgets used by the plugins/others frontend. To import components used here, use the path `$lib/plugins/{plugin_name}/`.
 - `pages`: This directory stores all the servable `.svelte` pages. These pages are later compiled to HTML during the ArgusDash build process. Each page *MUST* have its own subdirectory unless you only have a single page. Each page consists of two parts: A `+layout.ts` and a `+page.svelte`. You need both files. How each of them should be built up can be found [here](https://svelte.dev/docs/).

## Special files

 - `.gitignore`: If you are using `Git` version control, you are probably familiar with the `.gitignore` file. This file describes all the files that should not be tracked by `Git`. By default, `.gitignore` is configured to ignore any directories you would normally ignore during plugin development.
 - `package.json`: Although you plugin *should not* be uploaded to NPM, this file is needed to describe to `Node` dependencies used by your plugin. ArgusDash merges these dependencies into its own `package.json` and installs them during plugin installation.
 - `Plugin.toml`: `Plugin.toml` is the configuration file you have to provide ArgusDash on the plugins page. This file contains the most important informations of your plugin. Such as: your plugin's name, source location and version. Always configure the `schema` field under `[config]` as that specifies the layout and version of the `Plugin.toml` itself.
 - `readme.md`: A description of your plugin. As a matter of fact, you are reading one right now!
 - `requirements.txt`: A file listing all the `Python` dependencies. ArgusDash installs the dependencies listed during the plugin installation process.
