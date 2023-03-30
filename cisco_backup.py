from netmiko import ConnectHandler
class cisco:
    def __init__(self, username, password, host, device):
        self.username = username
        self.password = password
        self.host = host
        self.device = device
        self.net_connect = ConnectHandler(
            device_type = self.device,
            host = self.host,
            username = self.username,
            password = self.password,
        )

    def sh_version(self):
        return ("sh version",self.net_connect.send_command("sh version"))
    def sh_module(self):
        return ("sh module",self.net_connect.send_command("sh module"))
    def sh_env(self):
        return ("sh environment", self.net_connect.send_command("sh environment"))
    def sh_run(self):
        return ("sh run", self.net_connect.send_command("sh run"))
    def sh_boot(self):
        return ("sh boot", self.net_connect.send_command("sh boot"))
    def dir_bootflash(self):
        return ("dir bootflash:", self.net_connect.send_command("dir bootflash:"))
    def sh_ip_int_br(self):
        return ("sh ip int br", self.net_connect.send_command("sh ip int br"))
    def sh_int_br(self):
        return ("sh int br", self.net_connect.send_command("sh int br"))
    def sh_int_trunk(self):
        return ("sh int trunk", self.net_connect.send_command("sh int trunk"))
    def sh_vlans(self):
        return ("sh vlans", self.net_connect.send_command("sh vlans"))
    def sh_spanning_tree_summary(self):
        return ("sh spanning-tree summary", self.net_connect.send_command("sh spanning-tree summary"))
    def sh_port_channel_summary(self):
        return ("sh port-channel summary", self.net_connect.send_command("sh port-channel summary"))
    def sh_vpc(self):
        return ("sh vpc", self.net_connect.send_command("sh vpc"))
    def sh_vpc_peer_keepalive(self):
        return ("sh vpc peer-keepalive", self.net_connect.send_command("sh vpc"))
    def sh_cdp_neighbors(self):
        return ("sh cdp neighbors", self.net_connect.send_command("sh cdp neighbors"))
    def sh_logging(self):
        return ("sh logging", self.net_connect.send_command("sh logging"))
    def sh_inventory(self):
        return ("sh inventory", self.net_connect.send_command("sh inventory"))
    def sh_run_all(self):
        return("sh run all", self.net_connect.send_command("sh run all"))
    def sh_vpc_brief(self):
        return("sh vpc brief", self.net_connect.send_command("sh vpc brief"))
    def sh_int_desc(self):
        return("sh interface description", self.net_connect.send_command("sh interface description"))
    def sh_ipv6_int_br(self):
        return("sh ipv6 int br", self.net_connect.send_command("sh ipv6 int br"))
    def sh_ip_route_vrf(self):
        return("sh ip route vrf *", self.net_connect.send_command("sh ip route vrf *"))
    def sh_bgp_vpnv4_unicast_all_summ(self):
        return("sh bgp vpnv4 unicast all summ", self.net_connect.send_command("sh bgp vpnv4 unicast all summ"))
    def sh_bgp_vpnv6_unicast_all_summ(self):
        return("sh bgp vpnv6 unicast all summ", self.net_connect.send_command("sh bgp vpnv6 unicast all summ"))
    def sh_bgp_vpnv4_unicast_all(self):
        return("sh bgp vpnv4 unicast all", self.net_connect.send_command("sh bgp vpnv4 unicast all"))
    def sh_bgp_vpnv6_unicast_all(self):
        return("sh bgp vpnv6 unicast all", self.net_connect.send_command("sh bgp vpnv6 unicast all"))
    def sh_crypto_sessions(self):
        return("sh crypto sessions", self.net_connect.send_command("sh crypto session"))
    def sh_vrf(self):
        return("sh vrf", self.net_connect.send_command("sh vrf"))
    def sh_flash(self):
        return("sh flash", self.net_connect.send_command("sh flash"))
    def sh_hardware(self):
        return("sh hardware", self.net_connect.send_command("sh hardware"))
    def sh_tech(self):
        return("sh tech", self.net_connect.send_command("sh tech"))
    def sh_bootvar(self):
        return("sh bootvar", self.net_connect.send_command("sh bootvar"))
    def sh_ip_vrf_br(self):
        return("sh ip vrf br", self.net_connect.send_command("sh ip vrf br"))
    
    
    
class nxos(cisco):
    def __init__(self, username, password, host, device):
        super().__init__(username, password, host, device)

    def full_backup(self):
        commands1 = (
            self.sh_version(),
            self.sh_module(),
            self.sh_env(),
            self.sh_run(),
            self.sh_boot(),
            self.dir_bootflash(),
            self.sh_ip_int_br(),
            self.sh_int_br(),
            self.sh_int_trunk(),
            self.sh_vlans(),
            self.sh_spanning_tree_summary(),
            self.sh_port_channel_summary(),
            self.sh_vpc(),
            self.sh_vpc_peer_keepalive(),
            self.sh_cdp_neighbors(),
            self.sh_logging(),
            self.sh_inventory(),
            self.sh_run_all(),
            self.sh_vpc_brief(),
            self.sh_int_desc(),
            self.sh_ipv6_int_br(),
            self.sh_ip_route_vrf(),
            self.sh_bgp_vpnv4_unicast_all_summ(),
            self.sh_bgp_vpnv6_unicast_all_summ(),
            self.sh_bgp_vpnv4_unicast_all(),
            self.sh_bgp_vpnv6_unicast_all(),
            self.sh_crypto_sessions(),
            self.sh_vrf(),
            self.sh_flash(),
            self.sh_hardware(),
            self.sh_bootvar(),
            self.sh_ip_vrf_br()#,
            #self.sh_tech()
        )
        for i in commands1:
            my_file = open(i[0], "w")
            my_file.write(i[1])
