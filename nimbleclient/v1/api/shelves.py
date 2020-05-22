#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#
#   This file was auto-generated by the Python SDK generator; DO NOT EDIT.
#


from ...resource import Resource, Collection
from ...exceptions import NimOSAPIOperationUnsupported


class Shelf(Resource):
    """Disk shelf and head unit houses disks and controller.

    # Parameters
    id                   : ID of shelf.
    array_name           : Name of array the shelf belongs to.
    array_id             : ID of array the shelf belongs to.
    partial_response_ok  : Indicate that it is okay to provide partially available response.
    chassis_type         : Chassis type.
    ctrlrs               : List of ctrlr info.
    serial               : The serial number of the chassis.
    model                : Model of the shelf or head unit.
    model_ext            : Extended model of the shelf or head unit.
    chassis_sensors      : List of chassis sensor readings.
    psu_overall_status   : The overall status for the PSUs.
    fan_overall_status   : The overall status for the fans on both controllers.
    temp_overall_status  : The overall status for the temperature on both controllers.
    disk_sets            : Attributes for the disk sets in this shelf.
    activated            : Activated state for shelf or disk set means it is available to store date on. An activated shelf may not be deactivated.
    driveset             : Driveset to activate.
    force                : Forcibly activate shelf.
    accept_foreign       : Accept the removal of data on the shelf disks and activate foreign shelf.
    accept_dedupe_impact : Accept the reduction or elimination of deduplication capability on the system as a result of activating a shelf that does not meet the necessary
                           deduplication requirements.
    last_request         : Indicates this is the last request in a series of shelf add requests.
    """

    def identify(self, cid, status):
        """Turn on chassis identifier for a controller.

        # Parameters
        id     : ID of shelf.
        cid    : Possible values: 'A', 'B'.
        status : Status value of identifier to set.
        """

        return self._collection.identify(
            self.id,
            cid,
            status
        )

    def evacuate(self, driveset, cancel=False, dry_run=False, pause=False, resume=False, start=False):
        """Perform shelf evacuation.

        # Parameters
        id       : ID of shelf.
        driveset : Driveset to evacuate.
        dry_run  : Argument to perform a dry run, not the actual shelf evacuation.
        start    : Argument to perform the shelf evacuation.
        cancel   : Argument to cancel the shelf evacuation.
        pause    : Argument to pause the shelf evacuation.
        resume   : Argument to resume the shelf evacuation.
        """

        return self._collection.evacuate(
            self.id,
            driveset,
            cancel,
            dry_run,
            pause,
            resume,
            start
        )

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")


class ShelfList(Collection):
    resource = Shelf
    resource_type = "shelves"

    def identify(self, id, cid, status):
        """Turn on chassis identifier for a controller.

        # Parameters
        id     : ID of shelf.
        cid    : Possible values: 'A', 'B'.
        status : Status value of identifier to set.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'identify',
            cid=cid,
            id=id,
            status=status
        )

    def evacuate(self, id, driveset, cancel=False, dry_run=False, pause=False, resume=False, start=False):
        """Perform shelf evacuation.

        # Parameters
        id       : ID of shelf.
        driveset : Driveset to evacuate.
        dry_run  : Argument to perform a dry run, not the actual shelf evacuation.
        start    : Argument to perform the shelf evacuation.
        cancel   : Argument to cancel the shelf evacuation.
        pause    : Argument to pause the shelf evacuation.
        resume   : Argument to resume the shelf evacuation.
        """

        return self._client.perform_resource_action(
            self.resource_type,
            id,
            'evacuate',
            driveset=driveset,
            id=id,
            cancel=cancel,
            dry_run=dry_run,
            pause=pause,
            resume=resume,
            start=start
        )

    def create(self, **kwargs):
        raise NimOSAPIOperationUnsupported("create operation not supported")

    def delete(self, **kwargs):
        raise NimOSAPIOperationUnsupported("delete operation not supported")
