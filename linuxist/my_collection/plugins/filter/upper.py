from ansible.errors import AnsibleFilterError

def to_upper(value str):
    if not isinstance(value, str):
        raise AnsibleFilterError("The provided value must be a string")
    return value.upper()

class FilterModule:
    def filters(self):
        return {
                'upper_case': to_upper,
                }

