#!/usr/bin/env bash

VirtualMachineStatus() {
  status=$(vagrant status)
  case $status in
  *"aborted"*) echo "ABORTED" ;;
  *"not created"*) echo "NOT_CREATED" ;;
  *"running"*) echo "RUNNING" ;; 
  *"poweroff"*) echo "POWERED_OFF";;
  esac
}
status=$(VirtualMachineStatus)
case $status in
          NOT_CREATED) echo "Virtual machine not provisioned run 'provision' first" ; exit 0 ;;
  POWERED_OFF|ABORTED) echo "Virtual machine not running machine run 'start' first" ; exit 1 ;;
              RUNNING) ;;
                    *) echo "Error logining into virtual machine run 'restart' ; exit" ;;
esac
vagrant ssh1 2> /dev/null
if [ $? -eq 1 ]
	:
then
	:
fi

