from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    count: Union[Unset, None, float] = UNSET,
    scr_ids: str,
) -> Dict[str, Any]:
    url = "{}/ws/screeners/v1/finance/screener/predefined/saved".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["count"] = count

    params["scrIds"] = scr_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    count: Union[Unset, None, float] = UNSET,
    scr_ids: str,
) -> Response[Any]:
    """Most added to watchlist

    Args:
        count (Union[Unset, None, float]):  Example: 25.
        scr_ids (str):  Example: day_gainers.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        count=count,
        scr_ids=scr_ids,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    count: Union[Unset, None, float] = UNSET,
    scr_ids: str,
) -> Response[Any]:
    """Most added to watchlist

    Args:
        count (Union[Unset, None, float]):  Example: 25.
        scr_ids (str):  Example: day_gainers.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        count=count,
        scr_ids=scr_ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
