"""
FHIR Meta datatype.
"""

from datetime import datetime


class Meta:
    """
    Metadata about a resource.
    """

    def __init__(
        self,
        version_id=None,
        last_updated=None,
    ):
        self.version_id = version_id
        self.last_updated = last_updated

    def to_dict(self):
        data = {}

        if self.version_id:
            data["versionId"] = self.version_id

        if self.last_updated:
            if isinstance(self.last_updated, datetime):
                data["lastUpdated"] = self.last_updated.isoformat()
            else:
                data["lastUpdated"] = self.last_updated

        return data