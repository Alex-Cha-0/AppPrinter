import asyncio
from pysnmp.hlapi.asyncio.slim import Slim
from pysnmp.smi.rfc1902 import ObjectIdentity, ObjectType

oid_s = ("1.3.6.1.2.1.43.10.2.1.4.1.1", "1.3.6.1.4.1.40093.6.4.1")


async def run(ip, oids):
    for oid in oids:
        slim = Slim(1)
        errorIndication, errorStatus, errorIndex, varBinds = await slim.get(
            'public',
            ip,
            161,
            ObjectType(ObjectIdentity(oid)),
        )

        if errorIndication:
            print("error: ", ip, errorIndication)
        elif errorStatus:
            print(
                "ip:{}, {} at {}".format(ip,
                                         errorStatus.prettyPrint(),
                                         errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
                                         )
            )
        else:
            for varBind in varBinds:
                # print(model, " = ".join([x.prettyPrint() for x in varBind]))
                print(ip, varBind[1])
                return varBind[1]

        slim.close()

    # if model == "Pantum":
    #     object_type = oids["Pantum"]
    # else:
    #     object_type = oids["Other"]
    # slim = Slim(1)
    # errorIndication, errorStatus, errorIndex, varBinds = await slim.get(
    #     'public',
    #     ip,
    #     161,
    #     # ObjectType(ObjectIdentity(object_type)),
    #     ObjectType(ObjectIdentity("1.3.6.1.4.1.40093.6.4.1", "1.3.6.1.2.1.43.10.2.1.4.1.1"))
    #
    # )
    #
    # if errorIndication:
    #     print("error: ", ip, model, errorIndication)
    # elif errorStatus:
    #     print(
    #         "{} at {}".format(
    #             errorStatus.prettyPrint(),
    #             errorIndex and varBinds[int(errorIndex) - 1][0] or "?",
    #         )
    #     )
    # else:
    #     for varBind in varBinds:
    #         # print(model, " = ".join([x.prettyPrint() for x in varBind]))
    #         print(model, ip, varBind[1])
    #         return varBind[1]
    #
    # slim.close()
