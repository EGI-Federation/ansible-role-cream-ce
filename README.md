# CREAM CE role

This role expresses the UMD CREAM Computing Element.

## Requirements

None.

## Role Variables

None yet.

Variables are found in `defaults/main.yml`
Put your site variables in `../group_vars/cream-ces.yml` or `vars/main.yml`

## Dependencies

This role depends on the following roles:

  - EGI-Foundation.umd
  - EGI-Foundation.voms-client
  
## Example Playbook


```yaml
    - hosts: servers
      roles:
         - { role: EGI-Foundation.umd, release: 4 }
         - { role: EGI-Foundation.voms-client }
```

## License

Apache-2.0

## Author Information

<!--
Add the relevant contributors
-->
See AUTHORS.md