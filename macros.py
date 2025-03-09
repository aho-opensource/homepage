# see https://mkdocs-macros-plugin.readthedocs.io/en/latest/macros/
def define_env(env):
    """
    This is the hook for defining variables, macros and filters

    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """

    # add to the dictionary of variables available to markdown pages:
    #env.variables['baz'] = "John Doe"

    # NOTE: you may also treat env.variables as a namespace,
    #       with the dot notation:
    #env.variables.baz = "John Doe"
    @env.macro
    def resource( name ):
        #ret = R'[:material-cards-playing-heart-multiple: Resources](../resources/{}.md)'.format( name )
        #
        css_class = "ahopen-resource-link"
        resource_str = "Resources"
        svg_icon = R'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 4v18c0 1.1.9 2 2 2h12v-2H5V4zm16-4H9C7.9 0 7 .9 7 2v16c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V2c0-1.1-.9-2-2-2m-4.4 13.8-.6.5-.6-.5c-2-1.9-3.4-3.1-3.4-4.6C10 8 11 7 12.2 7c.7 0 1.4.3 1.8.8.4-.5 1.1-.8 1.8-.8C17 7 18 7.9 18 9.2c0 1.5-1.4 2.7-3.4 4.6"></path></svg>'
        # ^icon: :material-cards-playing-heart-multiple: 
        ret = R'<a class="{}" href="../resources/{}/"><span class="twemoji">{}</span> {}</a>'.format(  css_class, name, svg_icon, resource_str  )
        return ret

