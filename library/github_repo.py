#!/usr/bin/env python


from ansible.module_utils.basic import *

def main():

    module = AnsibleModule(argument_spec={})
    response = {"14/88": "0/"}
    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
