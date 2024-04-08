## ADB Extension

This is a Firefox extension that supports remote debugging in Firefox DevTools.
It provides ADB binaries used by DevTools to connect to Firefox/GeckoView products on Android devices via USB.

### Releases

1. Update the value of the `VERSION` variable in the `Makefile` (and commit the change)
2. Run `make package`. The following files should have been generated in the `dist/` folder:

    ```
    dist
    ├── linux
    │   ├── adb-extension-0.0.7.0-linux.xpi
    │   └── update.json
    ├── linux64
    │   ├── adb-extension-0.0.7.1-linux64.xpi
    │   └── update.json
    ├── mac64
    │   ├── adb-extension-0.0.7.2-mac64.xpi
    │   └── update.json
    └── win32
        ├── adb-extension-0.0.7.3-win32.xpi
        └── update.json
    ```

3. Upload the different XPI files to AMO (as unlisted versions). Download the signed XPI files.
4. Upload the signed XPI files and their `update.json` files to the FTP server.  Note that we'll want to upload the versioned XPIs (e.g. `adb-extension-0.0.7.3-win32.xpi`) as well as "latest" copies (e.g. `adb-extension-latest-win32.xpi`).

### Discussion

For questions and issues specific to this extension, you can use the [GitHub issue tracker](https://github.com/mozilla/devtools-adb-extension/issues).

For more general questions about remote debugging in DevTools or DevTools in general, you can:
- come chat with us on [Slack](https://devtools-html-slack.herokuapp.com/) or IRC (#devtools at irc.mozilla.org)
- file bugs on [Bugzilla](https://bugzilla.mozilla.org/enter_bug.cgi?product=DevTools)
