from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "email" VARCHAR(100) NOT NULL UNIQUE,
    "is_active" BOOL NOT NULL DEFAULT True
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlW9v2jAQxr9K5FdMYhNkZK3yDtCmdWpBYu00aZoikxzBqmMH+9I/Ynz3yQ4hIZAOqk"
    "4d0t6R5+7ie37Ed0tyzzQEiYyA63c3GhTxnSURNAHiO7vBtkNomtZCRkU65bYk06CsQqca"
    "FQ2R+M6Mcg1th0SgQ8VSZFIQ3xEZ50aUoUbFRFxKmWCLDAKUMeDctvTjZ9shTETwALp4TG"
    "+DGQMebXXMInO21QN8TK12IfCTTTSnTYNQ8iwRZXL6iHMpNtlMoFFjEKAognk9qsy0b7pb"
    "2ywc5Z2WKXmLlZoIZjTjWLF7IINQCsOPCTSGlyQ2p7x1u72z3vn7D73ztkNsJxvlbJXbK7"
    "3nhZbA6JqsbJwizTMsxpKb+dvs7x16wzlV+/FVa2oQNao6xALZq1JM6EPAQcQ4J77jdZ5A"
    "9q0/GX7uT1pe541xIhUN8w98tI64NmSolhQhoYwfg3BTcIr8up1DAHY7zQRtbBsh0wENkd"
    "3t+RIHUnKgouEuV+tqNKdS8ufgLISSZznJCqAbws8C+gS/wXh8aZpOtF5wK1xc1zjeXA0+"
    "Tlpdi1cvOEMoL7uZkLP1hNyMzCkNb++pioKdiHRlU+5uKHGTukIFjS0h49O4qq6OPigWzh"
    "s3yzr8591Cy8T/y+WElssdKG1aOmIwVkpeZjQecpdfcji6nnfAcHQ9r3E42tj2cDT34wiI"
    "6/TTBPhXtksoBUJ+B7chfvk6Hu2HWCmpgYxYiM4vhzON/ybQVTM/43druxTYWlf973Wiw8"
    "vxwPqXGmNl32JfMHjtPbP6DbELEZk="
)
