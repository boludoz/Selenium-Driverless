import pytest


@pytest.mark.asyncio
async def test_isolated_execution_context(h_driver):
    await h_driver.get('chrome://version')
    script = """
            const proxy = new Proxy(document.documentElement, {
              get(target, prop, receiver) {
                if(prop === "outerHTML"){
                    console.log('detected access on "'+prop+'"', receiver)
                    return "mocked value:)"
                }
                else{return Reflect.get(...arguments)}
              },
            });
            Object.defineProperty(document, "documentElement", {
              value: proxy
            })
            """
    await h_driver.execute_script(script, unique_context=False)
    src = await h_driver.execute_script("return document.documentElement.outerHTML")
    mocked = await h_driver.execute_script("return document.documentElement.outerHTML", unique_context=False)
    assert mocked == "mocked value:)"
    assert src != "mocked value:)"
