# Creating a new event entry

1. Open `_events/event.template` or `_events/event.template.simple`
2. Save a copy as `_events/<YEAR>-<MONTH>-<DAY>-<TITLE>.md`; e.g. `_events/2011-01-20-test.md`.
3. Modify as you see fit.  Create multiple sessions within the event by creating a list of objects under the `session:` key.

On a `page`, these tokens can be used:
* "$BUCKET" will be replaced with the URL in `_config.yml:path_to_bucket`.  This is used for pointing to assets on Amazon S3.
* "$IMG_PATH" will be replaced by `page.img_path` (which can itself use $BUCKET).
* "$DOC_PATH" will be replaced by `page.doc_path` (which can itself use $BUCKET).

### Table of contents

  * TOC
  {:toc}

### To serve locally

`bundler exec jekyll serve`

For some reason, this isn't working on my laptop as of 2018.  But it works fine if I push to github.
