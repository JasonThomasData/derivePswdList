### Simple program for generating lists of passwords to mark as weak

Users will commonly sign up for a service, like Facebook, and create passwords like `F@c3b00k`. A lot of them think this is really clever. It's really not clever, since attackers know people think it's clever.

I made this program to generate all possible strings in a formal system, starting with a string, and using rules of derivation (like `e=>3`, `a=>@`, `s=>$`), to derive new strings.

This program was trivial to write.

### Using this

At the CLI, use:

    derivePswdList <base_string>

That should give you a list of strings in a file by the name of the base string. By default `lower=>upper` and `upper=>lower` string transformations are turned off. Uncomment those in the `__main__` block if you like. However, doing so takes too long for me.

