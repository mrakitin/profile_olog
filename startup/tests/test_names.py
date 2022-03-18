import io
import uuid

import pytest
import requests
from pyOlog import SimpleOlogClient


def test_attachment_names(logid=1180):
    name = str(uuid.uuid4())
    fname = f"{name}.txt"
    body = "test"

    attachment = io.StringIO(body)
    attachment.name = fname

    olog_client = SimpleOlogClient()

    olog_client.update(
        log_id=logid,
        text="text",
        logbooks="Data Acquisition",
        attachments=[attachment],
    )
    res = requests.get(
        f"https://epics-services-tst:33181/Olog/resources/attachments/{logid}/{fname}",
        verify=False,
    )

    print(res.text)
    assert res.text == body
