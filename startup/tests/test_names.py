import io
import uuid

import pytest
import requests
from pyOlog import SimpleOlogClient

# body = ["t", "te", "tes", "test", "test1", "test-2"]
string = str(uuid.uuid4())
body = [string[:i] for i, x in enumerate(string)]

multiples_of_4 = []
for i in range(25):
    s = str(uuid.uuid4())[:4]
    if i > 0:
        s = f"{multiples_of_4[-1]}{s}"
    multiples_of_4.append(s)


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
    assert res.text == body, f"'{res.text}' (len {len(res.text)}) != '{body}' (len {len(body)})"
    assert len(res.text) == len(body)


@pytest.mark.parametrize("body", multiples_of_4)
def test_body_multiple_of_4(body, logid=1180):
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
    assert res.text == body, f"'{res.text}' (len {len(res.text)}) != '{body}' (len {len(body)})"
    assert len(res.text) == len(body)
