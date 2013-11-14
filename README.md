orgmode2json
============

A simple [orgmode](http://orgmode.org/) to [JSON](http://json.org/)
converter. It is most useful to work with tagged notes, but not any other
stuff (so far).

FAQ
---
* What is the license?
  All code is licensed under the [GNU Affero General Public License v3](https://www.gnu.org/licenses/agpl-3.0.en.html) unless explicitly stated otherwise.
  I am willing to talk about other options.

* Isn't the design rather byzantine?
  Yes and no. A way shorter script might suffice. While this is correct with
  respect to short-term payoffs the enforced modularized design facilitates
  greater testing in detail and reuse in the future.

* Were is the documentation?
  It is in the source-code. You can extract it using [sphinx](http://sphinx-doc.org/) if you want to.

* Are there tests supplied?
  Yes, of course. Just run `py.test` to see what causes trouble.
  Run `coverage report -m` to satisfy your OCD tendencies

* Why didn't you include feature X? 
  I most likely have other things to do. You can fork the code and send me a
  pull request if you are desperate.