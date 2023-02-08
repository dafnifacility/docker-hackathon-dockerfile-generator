import jinja2


def main():
    ## Call script to clone git repo.

    ## Get the contiguration

    ## Choose correct dockerfile template.
    template_env = jinja2.Environment(
        loader=jinja2.PackageLoader("dockerfile_generator"),
        autoescape=False,
    )
    template = template_env.get_template("python.jinja")

    # Render template with vars and write out.
    vars_ = {"foo": "hello"}
    print(template.render(**vars_))

if __name__ == "__main__":
    main()
