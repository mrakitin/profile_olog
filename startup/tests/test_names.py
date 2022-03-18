import io
import uuid

import pytest
import requests
from pyOlog import SimpleOlogClient

# body = ["t", "te", "tes", "test", "test1", "test-2"]
string = str(uuid.uuid4())
body = [string[:i] for i, x in enumerate(string)]


@pytest.mark.parametrize("body", body)
@pytest.mark.parametrize("newline", [True, False])
def test_body_attachment(body, newline, logid=1180):
    if newline:
        body = f"{body}\n"

    name = str(uuid.uuid4())
    fname = f"{name}.txt"

    attachment = io.StringIO(body)
    attachment.name = fname

    assert attachment.getvalue() == body

    olog_client = SimpleOlogClient()

    olog_client.update(
        log_id=logid,
        text="text",
        logbooks="Data Acquisition",
        attachments=[attachment],
    )

    res_url = f"https://epics-services-tst:33181/Olog/resources/attachments/{logid}/{fname}"
    print(f"\n  res_url = {res_url}")

    res = requests.get(res_url, verify=False)

    print(f"  text = {res.text}")
    assert res.text == body
    assert len(res.text) == len(body)


# @pytest.mark.parametrize("body", body)
# @pytest.mark.parametrize("newline", [True, False])
# def test_body_atch(body, newline, logid=1180):
#     if newline:
#         body = f"{body}\n"
#     name = str(uuid.uuid4())
#     fname = f"{name}.txt"
#
#     atch = io.StringIO(body)
#     atch.name = fname
#
#     olog_client = SimpleOlogClient()
#
#     olog_client.update(
#         log_id=logid,
#         text="text",
#         logbooks="Data Acquisition",
#         attachments=[atch],
#     )
#
#     res_url = f"https://epics-services-tst:33181/Olog/resources/attachments/{logid}/{fname}"
#     print(f"\n  res_url = {res_url}")
#
#     res = requests.get(res_url, verify=False)
#
#     print(f"  text = {res.text}")
#     assert res.text == body
