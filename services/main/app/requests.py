import typing

import aiohttp
from fastapi import HTTPException

from config import SERVER_AUTH_BACKEND, API, SERVER_EMAIL, CLIENT_NAME


async def get_user(user_id: int) -> dict:
    """
        Get user
        :param user_id: User ID
        :type user_id: int
        :return: User Data (profile)
        :rtype: dict
        :raise HTTPException status: Bad response
    """

    async with aiohttp.ClientSession() as session:
        response = await session.get(url=f'{SERVER_AUTH_BACKEND}{API}/profile/{user_id}')

        json = await response.json()
        if not response.ok:
            raise HTTPException(status_code=response.status, detail=json['detail'])

    return json


# async def get_client() -> dict[str, typing.Union[str, int]]:
#     async with aiohttp.ClientSession() as session:
#         response = await session.get(url=f'{SERVER_EMAIL}{API}/clients/name?client_name={CLIENT_NAME}')
#