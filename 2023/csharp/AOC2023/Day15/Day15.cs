﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Text.RegularExpressions;
using AOC2023.Utilities;

namespace AOC2023
{
    class Day15
    {

        public string input2 = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7";

        public string input = "slsv=7,bc=9,kbp-,cfr=3,slxgsf=7,bz=1,nbp-,svj=4,nbp=9,dz=7,mmqm=4,xjs=6,kdvhk=6,lgt-,gc-,sdjv=8,jfpvgt=5,zm=2,hbpmm-,pvb=9,bs-,dpj=4,vcp-,tvv-,pr-,bmx=9,mdc=2,pmpv=9,gdfgc-,krn=1,hpk=4,bcdsz-,pj-,vhlkz-,kcg=4,fxnk-,vvv-,cfr-,hbpmm=5,gr=8,lks=3,nqrdmh-,xksq-,zv=6,qpl-,lc-,ssnbtj-,cbslp=5,vhsd-,dkt=1,vg=7,cvd=2,vq=1,kjkt-,rrdkm-,dtsx-,slhkm=7,gc-,zk-,fdkfc-,lr-,pmpv-,mzzg=6,zpplm-,qmft-,dlrz-,xbrg-,vg=7,lp=6,fmg=7,jrb-,rjz=6,jnmz-,qlf=9,kfk-,hcsbqm-,bc=5,ll-,xczgt-,hn=9,lmfg=4,mgx=6,dvm-,qbvx-,zll-,lnl-,bs-,xdl=7,fl=7,bzxr-,prz-,nbp-,vpl=4,ppxtq-,mr=7,xdzch=5,gh=5,qdk-,crzsnh-,phc-,szgp=2,cmsg=2,jgxj-,tpqd-,bbh=1,hn-,ljm=4,pfdjc-,rsnr-,kbp=3,xxv-,fsrk-,nqrdmh-,cbj-,zctgz-,vs-,cmsg=5,pmv-,zm-,vvv=3,mj=5,vjzc-,xl-,mbz=8,jd-,dqrf-,gl-,zngc-,qj-,fg-,qt-,bz=9,nvc=3,pvb-,qz=2,pnxx=4,cjj=7,chc-,mzzg=3,fmg=1,hbpmm-,jj=7,hrppv=8,hkgz=2,sfp-,tvv-,zmqld-,nbk-,lp=3,rx-,srf=1,mf-,xhqm=1,vc=2,gdcv=8,rn=6,bs=1,kj-,rsnr=8,dvf-,dq-,knvm-,szqz=9,lrrt=3,fvbcj=6,qvd=1,qp=5,mht=1,dz=4,nvc=7,cbslp-,xs-,ln=2,qp=7,dhd-,kx=5,rqjm-,xs=1,nxc-,df=9,txpl=7,phc-,szqz-,nln-,vgvf=4,qm-,hm-,xs-,lp-,mr=9,gvn=7,txpl-,pj=3,ppzjql-,hrppv-,jmd-,mj-,bmx=1,jbt=4,lrrt-,bxt-,kphvsd-,hdf=6,zm-,vbbzrn=5,qvd=7,gtms=3,dz-,dhj=9,kd=3,vpm-,qfb=3,jj-,ph-,nkf-,jrv-,lp=9,fmf=8,mxn-,dq=5,bvxnx=6,jdn-,lz=4,vxpg-,lnl=1,sh=3,gr=5,fl=3,tpqd=4,jc=6,fjg=3,lmfg=6,tbm-,kcvqv=9,jmml-,mhj-,lc=5,qbvx=3,nln-,chc=1,jjf-,zngc-,zfb=8,xc=4,ckk-,nbp-,pb-,hbbsq-,bp=6,ln=5,zqs=1,rqjhl=8,hq=2,pmv-,cvd-,mt=7,lks=3,qfb-,zqmhf=7,dpc-,jt=3,mj=3,lq=5,lrrt-,dcb-,lnl=4,brm-,bc-,trdd=6,mr=4,jd-,bmx-,lmg-,dqrf-,zbp=9,hsv=1,ksh=1,mjq-,hxv-,knfmt-,rnj=8,bg-,trdd=6,clrt-,sdjv=8,svj=6,cz=2,rxqbqv-,fhgtq-,knvm-,mlh-,rmn-,sm-,dhd-,cjj=4,vhd=4,hcsbqm=7,rqjm-,pmv=8,mcm-,fmf=6,jc-,mk=8,mbz=5,nvc=5,drc=3,vg-,lz=5,fsqpbs=5,rjjg=2,zcm=8,hbfb=4,rsnr-,mzzg-,jmd=2,rxlbkl-,qt-,pl=1,dsv=1,jz=5,fk=1,gn=3,rp=1,mv=8,pts=6,dlf=5,hrppv-,vv-,dfzxj=4,trdd-,qc-,hm-,qdk-,qc=8,zm-,kphvsd=2,tz=3,rz-,bbh-,hs=9,dtsx=1,xsg-,bs-,vq-,qlq-,fxrl=4,rz=5,txpl=4,jfh-,lgt-,km=3,sf-,pnxx=9,sfx=9,gkkgm=7,pjfrs-,bs=5,hc=5,mtv-,srl-,npr=5,rxlbkl-,pmz-,ljq=2,mdc=4,brr-,pv=1,qcn-,xs=6,prz=8,qms-,mjrl-,tvv-,vjzc-,llb-,vhlkz=9,xf-,bz=5,nbk-,pfdjc-,bvxnx-,thhjcn-,krp-,vq-,hbql-,ndhfx=3,hzkxnp-,nrf-,qhl-,rqjhl-,ndhfx=2,bkc-,zklc=6,pmv=6,rjjg=3,thpc=2,qj-,vhd=8,gn-,dpc-,xhqm-,sr=8,jdn=7,bmb-,sn-,thpc=7,zngc-,bxhr-,llx=5,ml-,ph=4,kpn-,bds=9,kphsqq-,bxhr=9,xpj=3,njt=4,pnxx=6,ml=3,qnl=8,jmd-,cfr-,qfxmp-,zz-,jj-,hxv-,bf=1,mlh=7,jng-,ghnbmj-,hxq=5,vhv-,vg-,lq-,qcn=3,smk-,ckcf-,rhp-,hq=7,dtxh-,shmm=3,mdc=4,gr-,ndhfx=5,rz=3,mhbk-,mcm-,dpfmm-,lrrt-,mxn-,dtxh-,tdqk-,kfk=2,xstflx=5,dtf=8,rmjn-,mcm-,ccb=4,lm-,kzbr-,trdd-,mn-,sl=2,dp-,tb=1,qcn=7,vrd=4,pqff-,jc-,rqjhl=5,cvd-,xtv-,mn-,mx=3,bg=2,kzv-,bmh=7,xxv-,sdjv-,clrt=7,qcxq-,rs-,kln-,fd=5,fd-,rtnhrs-,ptgp-,gn=4,rz-,hv-,cbj=2,zpplm=9,fm-,tvv-,xdzch=2,xdl=4,hzkxnp=4,jfpvgt-,cz=4,nbp-,xpj=2,qt=1,dd-,vd=3,cz=6,zz-,sd-,rkt=8,qhrbk=7,lnl=5,zctgz=2,zfb=8,dpfmm-,gfj-,qd-,bc-,dpc=8,lks=8,rjz-,zzv=2,sn-,fpvpht-,bzs-,jc-,fh=2,jz-,bq=4,kzv=5,fqr=6,qn=9,bzs=6,mc-,vhsd-,cqk=9,mc=1,pqkf=4,gtms=2,sdjv=9,xjs=7,szqz-,szqz-,qdx=1,ffr=5,kpn=3,snm=7,kln-,dd=1,gdfgc-,zklc-,dk=3,dlf=6,rnj=3,pr=5,fk-,trjxdq-,pl=6,cvd-,vhlkz-,vhsd-,qcn-,jng-,gtms-,nvb=2,hbbsq-,mrt-,dz=5,pnxx=1,qm-,prz=8,skrc-,nxh=2,tp-,bhn=4,cbj=2,hbfb=9,vpm=8,hbpmm=6,zbq=8,sh-,lbqn-,hp=4,gj-,hsv-,trjxdq-,smvsp=2,lgt-,srdf-,srl-,fmf-,fh-,rmjn-,ll=7,ml-,fmf=3,kbp=8,fmg-,nx-,mx-,hphk-,vn=9,cbj-,pv-,dljx=2,sd=9,mj-,xs-,dljx-,dhj=4,qtb=3,bmx-,vpl-,pttv=3,dfxfb=6,hs=3,fdkfc-,thpc=4,ksh-,cqk=7,hpk=5,mclxh-,ffr=1,krc=3,hzplxp=6,zctgz=5,zzv=8,bs-,hz-,zrh=9,nbb-,lmfg=6,mgx=7,sfx=7,svj-,pr-,nhlmx-,qkbd=4,zbp=9,qm-,hsv=5,txpl=6,pgx-,xdl-,tb-,lgt-,rqjm=3,ccb-,svj-,hp=2,znr-,hbpmm=9,rnj=6,lnl-,ph=1,rrgz=8,bfl-,rxlbkl=2,rqdmb=6,mgx=2,vpx-,fg-,qms=8,cqk=6,gbx=3,qfb=5,dhj=7,xdl=2,hz-,krc-,jq=7,dqz-,vpf=6,mgx-,pr=4,mx=1,xhqm=6,km=7,hq=9,tjfr=9,dsv-,fxnk=8,vlvbk=7,mn=3,ph-,qj=7,ksh-,ksh-,lzg-,pmz=6,mkxr=3,zqs-,fk-,dq-,lklhn=4,mbg-,kj-,fhgtq-,jq-,vcp-,xj-,qp-,lq=8,jdn-,pmz=7,rzrx-,fttd=6,rjz-,gkkgm=1,fh=9,llb=6,jjxsf-,lklhn-,ckk-,sn=5,jgxj-,ndhfx-,pv=2,shmm=1,jbt=6,ppq-,zfk=7,lx=6,qcn=8,vxpg-,lbqn=5,bhn-,bp-,dfv-,mn=1,qcn=3,kjkt=2,qfxmp-,xstflx-,thpc=4,qpl-,prz-,krc=5,sm=1,gkr-,xhj-,hsv-,zgq=3,tq-,hd-,mjq=6,gdqpz-,pqff-,gdfgc-,fk=3,lkv=5,vxpg=1,cfr=7,mhbk-,ksh=8,hc=7,qz-,zzp-,fq=6,ccn=1,pfdjc=3,kj-,cstb-,zzp=2,gglrm=2,tx=7,vq=5,ck=1,fm-,thpc=8,pnxx=6,pv-,sr-,cbslp-,rn-,rzrx-,bpr-,dqz-,pt-,rxqbqv-,lgt=4,qcn-,zh-,tp-,lgt=9,dkt-,bpmqp=1,pt=1,jjxsf=8,kjkt-,vgvf=5,bmb-,mxn-,vkk-,hprj-,xhj=5,zgq-,bz=8,lrrt-,mj-,bgh=5,ffr-,vjzc-,rqkc-,cjj-,xxv=8,fm-,fxrl=7,lx-,sf=9,rqjm=6,pttv=2,xv=2,kphsqq=4,mc=9,qj-,qtb=2,qd-,nxh=9,dd-,vmhp-,xsg=6,fqr=5,jgxj-,srl-,trdd-,qdk-,hbql=1,bzxr-,szgp=8,zll=5,trjxdq=2,ls-,zzp=9,bfl-,rjz-,qhrbk-,lbqn=3,rn-,rjjg=3,mhbk=5,dtf-,hs-,bq=9,dcb=3,brm-,fmf=4,tp=3,pqkf=4,vcp=4,bq-,ghnbmj=9,pbf-,bds-,hdl=6,phpz=9,vkk=4,rnj-,jrb-,rj=7,dq=9,xxgf-,xjs=9,gn=2,hxq-,ghnbmj-,bq=4,szgp=5,ph-,zzv-,snm=6,mfh=4,dtsx=8,mbg-,qdx=2,qdz=8,qnl=2,rrdkm-,pfdjc-,xv=1,ls-,mzzg-,phr-,dsv-,rxlbkl=1,zzv=2,kx=9,zll-,zgp=5,fjg-,kln=3,slhkm-,bcdsz=2,zrh=7,tq=3,pttv=2,qdx-,kx=4,rn-,ls=3,xdzch-,mk=9,fd=6,lmg=5,spkk=4,jrv=8,dn-,tf=9,xj=3,qg=6,qd=7,bxt-,zgp-,ckcf-,qj=9,bxt-,phr-,ccb-,pjfrs=6,kzv=7,zb=1,tp=8,gkr=2,vpf-,xd-,mr=8,dcb-,rqjhl-,nbp=9,mdc-,ndhfx=1,nkf=7,lq=7,vs=3,fmf-,vpm=3,llx=8,sr=7,dpj=9,dtsx=8,rqdmb-,pjfrs=6,fmvd-,gp=2,gkkgm-,px=9,vhsd=3,zqmhf=6,zzv-,ptgp-,mfh-,xjs-,ll=3,xvj=8,ccn=2,mkqx-,qpl=9,dfxfb-,zrh=3,bpr=7,xbrg=8,xv-,cbslp=6,mbg=6,qdk=2,chc-,dfxfb-,vcp=1,vd-,lx=9,txpl=3,ccb-,zbp=2,ljq=4,zpplm-,dljx=9,tf=6,dtsx=2,qcxq=8,bpmqp=5,pc-,rsnr=6,pqkf-,bvxnx=3,xl-,bgh=2,zk=7,dqz-,qrv=1,xczgt-,gnjn-,xpj-,vpf=6,kjr=2,hzkxnp-,kphvsd-,lr-,mxn-,cxqjcn=2,sj=4,ln=3,bmb-,tpqd-,lrrt-,gfj=4,nbp=2,nxh=4,tl=3,pt-,ht=3,rhp-,hqmvs=1,bmb=4,kln-,ksv=2,zmqld=6,bmb=1,sr-,cz-,hxq=3,hd=1,rqdmb=2,bvsfx=6,qd-,pl=1,rn=4,vhsd=3,dkt-,fd-,fq=9,pjfrs-,mt=9,fvbcj=9,kzbr=3,kjkt-,mc=8,qfxmp-,ms-,nxh-,lks=8,fm-,qbvx=9,hv=7,ln=7,pmz=3,tf-,rrgz-,px=9,szgp-,srdf-,bf-,tjfr-,zndpm=5,fp=2,vvv=8,bp-,kfk-,qn=8,mrt-,xczgt=4,shmm-,hzplxp=5,fk=4,bpmqp-,hbpmm=6,fsrk=7,txpl-,fvq=9,ckcf-,szgp=2,shmm-,vxpg=1,hsv=9,pmpv-,dkt=8,vf=4,jjxsf=7,qmft=3,pv-,vgvf-,vpm-,lc-,cbj-,rrdkm=6,pgx=7,gh-,mhj=4,xsg=2,mlh-,tf-,fdkfc=9,ssnbtj=3,fhgtq-,xs=5,hvh-,hcsbqm=9,brr-,pc=3,dsv-,pgx=8,hz=2,xsg=6,hcsbqm=8,dhj=8,slsv=5,kphsqq-,vbbzrn=4,knpc-,qrvkj=7,mn=1,cqk-,ssnbtj=9,cmsg=4,xbrg=7,lkv-,jd=8,dqz=6,zll=9,rrdkm-,dfxfb-,mbz-,vpf-,sm-,pv-,mmqm=1,krn-,trjxdq-,dljx-,mht-,cbslp=3,gj-,zcm-,hgn-,vvv=6,vhsd=1,thpc=3,vbbzrn=1,xjs-,mkqx=5,hs=4,bcdsz-,dlrz-,lmfg=6,cbj-,jdn-,nbk-,rp=7,vgvf-,vgvf=6,km=8,lxdv-,zh=4,fk=1,dfzxj-,vmhp=1,qp=1,srl=9,bq=2,ht=4,pmz-,ttvr=7,kcvqv-,xq=2,pbf-,dpfmm=9,zbp=6,gkr-,gr-,mdc=3,bzs=6,hzplxp=6,jdn=7,bvxnx-,brm-,nkf=3,qms-,nln-,xl-,lpx=6,jgxj-,qdx-,px=4,mhj-,jbt-,qz=5,knfmt-,mfm-,bxhr-,zv=5,gvn-,vc-,dlrz=8,lz-,qhl-,kcg-,qdv-,rj-,hxq=8,lm-,zpplm-,tx-,thhjcn=6,qmft-,pc-,mjrl=4,zv=5,fsrk-,drc=1,lpx-,srdf-,bg=6,gfhl-,qj=5,vn-,zh-,ml-,gkr-,rzrx-,pl=7,sf=2,bg=9,fm-,hphk-,xj-,xgb-,fd=8,kln-,tq-,krp-,qcxq=4,rnj=9,svj=6,zpplm-,zgp=8,pj=9,qnl-,lmfg=6,dnfh=6,zzp-,mcm=4,szqz=4,dd=2,thhjcn=8,nvb-,ptgp=6,ccb-,hkgz=9,bkc-,dfzxj-,knpc=7,lzg-,dk-,cfr-,gmtq-,pttv=4,tp-,kzbr=9,qm-,dpj=4,bmtf-,jgxj-,bzxr-,bhn=9,nln=8,bzs=3,qtb-,hbbsq=1,ljm=8,bhn=9,qfb-,ll-,hcsbqm=8,rkt-,rqjhl=4,fvq-,bf-,dpfmm-,mtv-,xczgt=1,knvm=7,ttvr=3,qmft=7,sl=5,mcmmvv-,vrd-,bq=8,fk-,ckcf-,vpm=3,tp-,zfb-,nxc=3,gbx=2,krn-,sfp-,df-,nt=6,vpl-,qbvx=2,cfr-,fd=9,bs=6,qdx-,hdf-,mf-,rc-,vpx-,pt=3,dp=8,rs=7,gp=9,tz-,zqqv-,hbbsq=5,sfx-,fvq=5,kjr=4,dk-,cbj=4,gnq-,nx-,tx-,zx-,sj=9,hqmvs=8,mj=8,hcsbqm=5,gbx=9,clrt=3,mt-,qcxq=2,sr=4,kx-,rcts-,zrh-,zb=1,tvv=2,hbfb=4,fp-,hbbsq=2,mj-,mfh-,snm-,hzkxnp-,jb=2,jd=5,zpplm=9,df-,xksq-,cxqlmd-,jc=4,hp-,fvbcj=9,dsv=7,jng-,pl-,rrdkm-,fl-,xxv-,brm=1,px-,lc-,ghnbmj-,drc=5,dtf=2,hzkxnp-,tq-,zk-,tbm-,tl-,dljx=1,vgvf-,gdfgc-,bxhr-,hd-,xhj=8,qbvx-,nxh-,szqz-,lc=2,bq-,qmft-,vvv=8,bcdsz-,tf=4,lc-,tpqd=7,xxv=8,qdk-,qkbd-,rp-,rmjn=1,ppr-,hpk-,zmqld=3,gp=8,vhsd=8,vvv-,tvf-,jq-,jz-,pqff-,hq-,rx-,sdjv-,szgp=5,rc=8,qfb-,qmft-,jz=2,mfm-,fmvd-,gmtq=4,trdd=7,dnfh-,fsrk=3,dlf=9,vvv=8,mxkr=1,vpf=5,rqjhl=4,pjfrs-,xv-,fl-,fpvpht=2,qfxmp-,hz=4,zll=6,phr-,vd-,hm=9,xvj-,px-,hcsbqm-,fvq-,fmvd=8,prz=7,ljq=6,prz=2,qm=1,dp-,mv-,thhjcn-,lklhn-,fk=8,txpl=3,hrppv-,hxq=6,qj-,kdvhk-,hln=6,sh=4,ncz=8,sfx=6,hn=2,ll-,tb-,bf-,ml=4,dhj-,drc-,trdd-,lmfg-,dvf=6,zqmhf-,qg=4,dfzxj-,bbh-,srdf=3,pqff-,vgvf=2,gfj=1,bgh=4,hzkxnp-,txpl=9,ppq-,pmpv-,pc=1,pfdjc=9,qdv=9,szqz=4,spkk=2,mdc-,kcg-,mj=6,pts-,mbg=7,kcvqv=7,hdl-,mdc-,mn-,pqff=2,gl-,nt-,gfj=6,srdf=9,dnfh-,srl-,ppr=7,mj=3,qhl=5,mht=7,gnjn-,qms-,ll-,bmtf-,qc-,pc=5,sfx=2,dz=3,zz=2,slsv-,zp=7,ffr=6,hvh=4,dz=6,pgx-,rkt=1,mkqx=5,gc-,vmhp=6,ksrg=3,qrvkj-,pfdjc=7,cqk=1,zh-,bf=3,ll=9,vs=2,srf-,bpr-,thpc-,fl=1,sl-,zrh=9,bs=5,ppzjql-,hm-,dh=1,ndhfx-,gfhl-,dn=9,nbk=7,svj-,xvj-,srdf=5,phr=7,mv-,lx-,svcx=5,qk=2,bg-,zbp-,mx-,kj=2,fhgtq-,ljm=7,ghnbmj-,phr-,lrrt-,rtnhrs-,cg-,gvn=1,qm=5,zqqv-,pr=2,gmtq-,ppzjql-,fhgtq-,fttd=7,smk=4,gnq-,mclxh-,xjs-,hsv=4,gl-,srl=5,hsv=6,ml=2,gtms-,vkk=8,rrgz=6,cvd-,thhjcn=3,qp-,mhbk=7,vjzc=1,vq=5,hbfb-,df=2,pbf=1,jc=4,nbb-,ssq=4,sh=5,ttvr-,qkbd=1,jc=1,qp-,nkf=5,cfr-,mt=4,lgt-,rqkc-,pqff-,qj=1,kjr-,clrt-,bpr=2,qk-,xpj=3,xtv-,zv-,dljx-,gkr-,zqs-,thhjcn=4,mfm=3,fm=3,ph=2,skrc=6,tx-,mlh=9,ffr-,zk-,km-,svj=6,hzplxp=2,mdc=9,hx=9,df-,qkbd-,zmqld-,hsv-,tf-,zm=1,pb-,gbx=5,bzs=4,zzp=8,zm=4,knvm-,qcn-,thpc-,rqkc-,hbfb=2,gdfgc=1,hq-,dtxh-,fdkfc=9,plh=3,sd=8,rs=9,zp-,sm-,jb-,dtxh-,fl=5,bbh=1,xvj=5,tvv-,zzv=9,jdn=8,kjkt=6,ppxtq=7,jb=1,vhsd-,shmm=3,gdfgc-,gdqpz-,kjr=6,gdqpz-,mkxr=4,qfb-,bhn-,thhjcn-,hln=3,dqrf-,kzv-,sfp-,rrgz-,pk=8,dtxh=7,trdd=3,hsv=7,vlvbk=8,fmg-,jc=5,qfxmp-,gkr-,tx-,fsqpbs=2,bvsfx=4,hbpmm=7,vjzc-,vxpg=1,hc-,mgx=4,kphvsd=9,thhjcn=1,mht=4,qdv=9,hc=7,kbp-,qj-,sd-,dvm=5,jng-,bxt=3,fv-,rmjn-,jq=2,bs-,xhqm-,rz=1,xxv=8,rzrx-,thpc-,fqr=4,kcg=3,dz=2,rc-,fk=3,bmtf=1,gp-,hln-,zxl=4,kcg-,lp-,kcvqv-,bz-,prz=4,nvc=1,mj=9,tk=1,fmg=5,fvq=2,vx-,kcg=5,vd-,rhp=2,pmv=8,pts-,hs-,pl=1,krc=9,bpmqp=1,vrd=9,px=2,pb=5,qc=8,npr=6,gkr-,zzxnd-,bs=2,vxpg-,dpfmm-,bvxnx=1,gmtq-,ksv=1,nx=7,nxc=6,bbh-,jjf-,lm=1,hsv=9,srdf-,qms-,fsrk-,tvv=7,gkkgm-,phr=9,jrv-,nxc-,ccb=3,rc-,cstb-,zrh=3,bzxr=9,pbf-,xh-,spkk-,gh=3,kjkt-,tstvzh=4,fq=7,sm=4,mcmmvv=3,xdzch=3,sn-,trjxdq-,hn-,vgt-,rqjm=8,fv=6,bmh-,kpn-,zctgz-,qz=6,dz=7,bmb=9,zklc=4,rhp-,cjj-,clrt=3,cstb-,jt=4,nxc=9,hz=6,pc=2,ljm-,lm-,mn=4,gdqpz=2,dqrf=9,dpfmm=6,hln=1,hx-,tr=9,jq-,jqz-,nbp=3,nbk=6,zgq-,htc=7,cg=3,mxn-,hxv=9,xgb-,qz=6,qdk-,xpj=3,fhgtq=4,bkc-,vlrft-,gnq-,vpf=7,dnfh-,pjfrs-,zzp-,nvc=8,gtms=1,knpc=8,ndhfx-,mkxr-,lmg=5,cbj-,dvm=7,ssnbtj-,gkr-,qrv-,dcb-,ncz=3,qbvx-,mj-,mt-,lx-,trdd-,dqz-,kx-,fsqpbs-,gkr-,fdkfc=5,mr-,hxq-,vrd=2,cstb=2,drc-,shmm=7,fg-,mv-,vq=6,vcp-,fqr=6,fjg=6,slhkm=9,dh-,rsnr-,qbvx=8,hbpmm-,rmjn=7,dfzxj=9,mt-,bvxnx=7,pttv=9,vpx=2,qd=9,slhkm-,clrt-,xs-,skrc=9,fxnk-,mx=2,xdl=1,pts-,qm=2,gnq=2,lxdv=8,lr-,slhkm-,cbj=4,dpfmm-,cqk-,hbfb-,dtf=9,pj-,lz=2,bc=1,nxc=2,qg-,lq-,lnl-,vhd=9,hz-,rhp-,cz=9,zmqld-,phr=2,tt-,bxhr-,qhrbk=2,ht-,mrt-,rrdkm-,rjz-,ccb-,xc-,jfh=9,qhrbk=6,qhl-,ln=9,rn-,crzsnh=5,rtnhrs=8,dz-,cfr-,sl=4,mbz=7,thpc=6,mbg=5,qbvx-,dh=8,hcsbqm=9,bcdsz-,zzxnd=9,km=4,bfl-,gc=5,szgp=8,ln=8,bg-,fpvpht-,tstvzh=9,vhsd-,qtb-,mv-,zqqv-,ndhfx=9,hv-,tvv=8,krp-,qbvx-,thhjcn=4,vrd-,zqqv=2,kx=8,qm=6,jng=1,ms-,nxc-,crzsnh=3,dpfmm=7,krc=4,cmsg=9,vcp-,bzs-,fxrl=8,rrdkm-,mrt=6,jrv-,rx-,cg-,ppd=5,ht-,hm-,trdd=1,hbpmm-,qlq-,dpfmm=3,fsqpbs-,rmn=5,ppxtq-,zp=6,zqmhf-,xj=3,kbp=3,qkbd-,gn-,fjg=4,dhj-,qqnx=7,szqz-,mjq-,tb-,gr-,ncz-,qkbd=9,dfxfb=3,hsv-,nf=2,lnl-,tb=6,pj-,dm=6,qn=4,crzsnh=6,dhj-,skrc-,rx-,ltf-,bxt=5,vlrft-,gv=9,rs-,gmtq=9,ksh-,xhqm=7,jt-,kcvqv=7,tr-,gglrm=6,mfm-,cvd=7,gfhl-,zqqv=8,lrrt=5,rtnhrs-,rrgz-,jgxj-,gl=8,xc=7,gh=1,jz=6,dfv=4,kcvqv=5,nbp=9,knfmt=5,vhsd=6,vq=3,mxn-,vmhp=8,brr=9,snm=4,gp-,dlrz-,tjfr-,fvq-,dlrz-,qrv-,qm=5,zxl=8,zrh=7,gp=6,dgpl=1,dqz=4,ln=7,rp-,xhj=2,ncz=3,brr=2,rrdkm-,mbg=5,kmgb=9,dk=1,ppzjql=7,xd-,jjxsf-,nxh-,kz=5,mrt=3,xxgf=2,mdc=5,cmsg-,qfb-,gh-,rsnr=8,xdzch=8,gn=2,nqrdmh-,kjr=6,ppr=7,rtnhrs=4,xj=4,spkk-,qdk-,jt=5,pts=7,vmhp-,hzkxnp=9,hxv-,qvd-,ls=3,rzrx-,vpm-,zmqld-,mxkr=3,bxt=6,fl=1,qnl-,gtms=3,ppq=3,znr=5,ndhfx=5,nbk-,svj=9,cg-,gnjn-,bcdsz=9,gmtq=9,vlrft=2,dlrz-,qcn-,bg=4,ljq=5,mtv=5,kcg-,gbx=2,ghnbmj=4,bzs-,hgn-,fsrk-,rqdmb-,hgn-,bmtf-,zngc-,hxq-,srl-,nt-,fhgtq-,mbg-,xgb-,vhlkz=3,rqdmb-,mlh-,ssnbtj=2,knvm=3,vvv=9,dfv-,ppzjql-,spkk=8,bf-,sr=1,jrv=6,zm-,bzxr=4,dm=8,slhkm-,hprj=3,bfl=1,fsrk=9,bvxnx=6,hd-,kjkt=9,tq=5,fsqpbs-,fv=6,fd-,kzbr=8,vkk-,vpm=2,spkk=3,nqrdmh-,dpfmm=6,fvbcj=8,cqk=4,ttvr-,gkkgm-,zgp=6,sr-,mkqx=3,mhj=3,brr=5,zxl-,dfxfb-,jrb-,zfb=5,mcmmvv=3,ck=3,hsv=8,bc=7,srl=9,gvn=4,dn=6,fp-,zzv=6,bfl-,bmtf-,vhlkz-,nvb-,hsv-,xdzch=9,rqkc-,hdl=6,lxdv=6,kdvhk=3,mk-,dgpl-,phpz=1,kx=1,sfp=7,cxqlmd=9,rrgz=5,znr-,hxv=8,fk-,cmsg=6,kphsqq-,gfj-,vx=5,vpx=5,rhp=8,vv=9,rmn=5,fg=2,pgx=3,rqjm-,ls-,hz-,vmhp-,nrf-,mk=7,hzplxp=3,zx=6,gnq-,clrt=4,ksrg=8,skrc-,phpz=9,mtv=9,lr-,qfb=2,kj=2,pmv=6,qbvx-,mjq=9,dlrz-,xvj-,vg=3,jj-,qnl=7,mhj-,kpn=1,qbvx-,gh-,ccn-,bf=9,rrdkm-,zzxnd-,vpl-,lmg-,jd=8,rhp=6,thhjcn=2,zcm-,zfb-,phc-,xq-,cxqlmd-,rqdmb=5,rrdkm=1,zz=5,pb-,trjxdq=7,jrv-,dgpl=7,chc-,gl=4,zbq=4,pnxx-,mf-,jfpvgt=1,qdx=4,hp=3,gn-,llb-,zp-,cxqjcn-,lks-,phc-,dk-,phpz-,mht=6,fqr=8,mhbk-,vbbzrn-,npr=7,kpn=9,hdf-,lzg=6,kphsqq=5,vhv-,ltf-,mbg=4,hzplxp-,qm-,hbql=1,pgx-,gtms-,smk-,mclxh=3,tvv-,zfk=7,zctgz-,hn=4,bgh=9,nvc=4,xgb=2,nln=2,vlrft-,vhsd-,mrt=3,skrc=5,cxqjcn-,gdfgc=6,zngc=4,krn=8,pmpv-,xhj=4,dtsx-,qn-,xksq-,fg-,gfj-,dqrf-,mbg-,dq=3,hgn=5,hln=1,zk=4,qvd=1,xxv-,mf=1,vv=3,rjjg=5,hbpmm-,bzxr-,qrvkj-,kjkt=8,dh-,jqz-,gp=2,krc-,hphk=6,fmvd=2,kjr-,qj=1,vn-,xtv-,srl=2,dtxh-,hz-,bz=5,lx-,jj-,cz-,fk-,jfpvgt=6,dsv-,lmg-,pjfrs-,fvq-,zzp=6,kmgb-,zqqv=2,lzg=7,mfm=7,hdf-,fq-,nt=4,mjq=8,vgt-,hkgz-,xdl=5,hvh=2,brm=8,kjxq=2,xxgf-,znr=4,lmfg-,trdd=1,mfh-,dsv=3,clrt=1,xstflx=6,xksq-,dtsx-,jfpvgt-,ms-,gtms-,px-,rs=5,gvn=3,pr=9,svcx-,sn-,jj-,vpm-,xdzch-,bf=4,pnxx-,mlh=3,zqqv=7,cmsg=4,npr-,mxn-,ck-,cxqjcn-,szqz-,dqrf-,brr=1,gkr=6,ghnbmj=7,fd=4,fm-,kjr-,vg-,pk-,dn-,qp-,qtb-,rsnr-,mclxh=5,hpk=3,qcxq=1,cz=9,gdqpz=4,llx-,tdqk-,mk=7,jfh-,rzrx=9,gnq-,dkt-,ncz-,kz=1,xtv-,fmf=2,vf-,plh=3,ppzjql=1,vx-,dtf=6,mc=9,znr=9,szqz-,mfm=3,sn-,nbb-,jdn=5,sl=4,qtb=6,knvm=4,pbf-,hpk=5,lnl-,bkc-,bmtf-,qrvkj-,hrppv=1,cmsg-,cbslp=4,trjxdq=4,qhrbk-,jc-,sd-,zfk-,srdf-,mxn=3,bs=5,spkk-,hkgz=6,gfj=7,nkf=3,qqnx=4,xf=1,qk-,tr=8,fd=2,mcm-,mbg-,dlrz=5,mr-,srl=2,zp=8,ck-,tt=2,cbslp-,ksrg=3,rzrx-,zzxnd=3,qlq=9,qmft-,hz-,zzxnd-,hzkxnp=4,vgvf=1,shmm-,mdc=4,dtf=3,dljx=7,rs-,hq=1,zmqld=4,sl=1,vx-,zx=8,xc=3,knpc-,cqk-,zbp=8,hbql-,ljm=9,nqrdmh-,gv=5,kln=1,htc=1,fm=6,vhd=3,mzzg=8,jjxsf=2,tf-,xczgt=1,tf=8,xdzch=6,rqkc-,mhbk=8,qp-,gmtq=2,ms-,qbvx=1,cxqlmd=1,npr-,ml=8,krn-,xtv=7,qnl-,mfm-,rhp-,bfl=7,gkkgm=1,dqrf=7,jc-,trdd-,lq=1,nvzj=8,jrb=3,pvb=1,cstb-,vhv-,lmg-,qpl=2,qp-,brr=4,fdkfc-,xhqm-,hzkxnp-,bz-,cxqjcn-,gglrm-,sr=3,pjfrs=9,rc-,xgb=2,ppxtq-,dpc-,xh-,dfv-,hdf=4,hprj-,pmv=4,zbq=5,xq-,dhj=2,mkxr=2,hqmvs=3,cqk-,vhv=2,qhrbk=6,qvd-,cvd=7,qdx=4,zndpm-,lbqn-,lmg=7,szqz-,dq-,txpl-,bg-,pj=1,mf-,fh=5,rjz=4,nln-,rj-,qdx=7,hxv-,pqkf=7,vhsd-,vhlkz-,zngc-,mjq-,pmv-,pmz-,km=1,vv=9,cxqjcn=6,dpc=2,fxrl-,gv-,gbx-,lm-,mclxh-,qtb=3,zbp-,zm=8,dh-,lmg=1,gp=6,kdvhk-,xs=3,zpplm=3,ppd-,dpc-,zqqv=1,lxqv-,qk=4,kpn=5,xv=1,qcn=2,cbslp-,fmg-,vkk-,zv-,jf-,sl-,hkgz-,llj=3,mf-,xs-,zqmhf-,lp-,ltf-,bgh-,mjrl-,fp=2,jgxj-,fdkfc-,rc-,sl=1,pj=3,zfb-,hz-,xgb-,fmg-,bg=2,hv-,kpn-,zmqld=6,qrvkj-,rrgz=5,dh-,thpc=5,krn-,vlrft=3,xpj=4,nt=2,mxkr=2,zqs-,ml-,gglrm-,vgvf-,zm-,dfxfb-,nbk=2,rqjhl=5,mfh=2,mj-,qdk=5,nqrdmh=1,rkt=3,zpplm-,qtb-,llj-,qcxq-,mf-,vgt-,tb-,bvxnx-,dz-,rrgz-,mhbk=2,zklc=6,tdqk=2,qdv=1,tdqk=5,dvf-,tpqd-,rxqbqv=3,rrdkm-,qcn=7,sfp=9,lklhn-,vd=5,fp-,rcts-,vpm-,cxqlmd-,dfxfb-,dlf=2,bvsfx=7,zz=9,pc-,xq=6,bq=5,trjxdq-,lzg-,hzkxnp-,kcvqv-,gdqpz=9,shmm-,zxl-,lrrt=5,jt=6,dpfmm-,mdc-,mdc-,krn-,rsnr=8,cstb=5,hzplxp=6,hv-,vhlkz=5,lq-,pr=4,bhn=1,crzsnh=1,ssnbtj=8,mmqm=4,xxv=3,rrdkm-,mv=1,mt=9,lks=7,cjj=1,hp=9,zz-,ndhfx=5,bds-,qhrbk=7,shmm-,smk-,dtxh=7,vc=1,bmb=2,kjr=6,zqqv=5,bxhr-,xj=2,kbp=3,lmg-,rxqbqv=5,rqjm-,lz-,fsrk=2,mcm=2,vq-,cbslp-,phc-,mxn-,gr=8,zk-,xc-,hpk-,dd=2,fq-,vrd=8,dljx-,kx=5,qdk-,dfzxj-,vg-,gdcv-,bq-,fdkfc=1,lq-,bxt=4,txpl=7,tvf=7,tstvzh-,fk=5,srdf-,krn=7,vvv=6,mjq=3,xxgf-,dz=2,xvj-,tr=9,mgx-,nf-,qhl=4,tf-,hsv=9,hs-,xl=3,jrv=8,phc-,pc=1,cbj-,hrppv-,lr=7,hln=4,hprj=8,vgt-,qj=5,dpc=9,dfzxj=6,vg=3,dqrf=4,fh=3,fl-,qms=7,qfxmp=4,jt-,phpz-,lnl-,ssnbtj=4,fsrk=1,tt=1,dq=3,qcxq=5,km=4,pdkdj-,kln-,nt-,rz=9,bp-,lgt=4,hprj-,xhj-,mkqx-,gnq=9,rtnhrs=1,bpmqp-,bmh=4,kjxq-,vq-,qj-,dnfh=1,nvzj=7,thpc=2,tl-,mmqm=5,gglrm=2,kdvhk-,gdfgc-,cbj-,qj=7,rrgz-,bf-,phc=4,qm=9,hc=7,vlrft=6,knfmt-,qrvkj-,mxn-,kphvsd=3,zgp=5,bg-,gdcv-,xsg-,cbslp-,bfl=3,lrrt-,bpmqp=5,hzkxnp-,smvsp-,hcsbqm=2,xsg-,hxq=8,mhj-,qrvkj=6,fsqpbs-,jz-,zngc=1,ffr-,vhd-,sr=9,hpk-,mmqm=2,vd=8,kmgb=2,jfh=9,xsg-,pmz=5,kjr-,nvc=5,hd=3,hxq-,ls=5,gnjn=7,vg=8,lk-,dgpl-,dgpl-,lp-,gn-,cxqlmd-,hs=9,npr=5,hrppv-,sl-,tp-,vv-,qn=2,vpm=3,zgq-,jfh-,pmpv-,mbg=3,znr=8,jrv-,pdkdj-,ppd-,bmx=7,rxlbkl-,fmvd=9,krc-,rmn-,kphvsd=6,jfpvgt=6,xtv=7,fvq=8,fk-,xdzch-,kjxq=2,bvxnx-,fh-,vhsd=9,vn=2,mtv-,zv-,mxn=6,mzzg=8,slsv=5,ljm=6,gh-,tvv-,jmml=7,kphvsd-,fpvpht=8,lm=3,ms=2,pbf-,mfm-,lbqn-,tstvzh-,gkkgm=1,lks=5,fh-,rmn-,dljx-,mhj-,mkqx-,sj-,pqkf=2,tx-,rtnhrs-,jz=5,jnmz=7,gv-,gdqpz=8,mrt=1,gj-,fk=9,tt-,rxlbkl-,cqk-,vpx-,sm=3,mht-,kd-,ppd-,zgq-,jjf-,kbp=4,rc-,jjxsf-,phc-,vxpg=1,ckcf-,lxdv=9,zfb-,qvd-,tstvzh=4,fjg=6,gdfgc=8,xxv=6,vlvbk-,nxc=9,zb-,vpl-,lks=6,hz-,dd=3,nln=5,mdc=7,dcb-,ttvr-,pv=5,thpc-,qhl-,dn-,mr-,zqqv-,njt-,gdqpz=8,rhp=5,slhkm=5,pmv-,mcm-,rsnr-,hbql=9,srf-,bpr=7,bq-,ls=8,zqmhf-,hsv-,vbbzrn=7,vv-,cmsg-,fg=7,kdvhk-,nbb=6,zngc-,mhj-,zfb=3,jjxsf=7,zpplm-,vpl-,mht=8,kzv-,jf=3,ksh=4,cstb-,gvn-,qtb-,rx-,txpl-,spkk=5,vmhp-,lxdv=9,hzplxp-,vmhp-,lxqv-,qrv=3,dhd-,ssq=6,sr=9,gn=3,gdfgc=2,vhv-,xtv=2,xxv=9,sm-,ssq=9,vkk=8,nln-,gh-,pr=5,dq-,fl-,xhqm-,llb=7,mtv-,rzrx-,bgh-,vxpg=3,ll=8,rqjhl=9,mx=5,hsv=6,ppxtq-,jmml-,gvn=6,vlvbk=3,slhkm=5,mtv=6,rmn=6,pvb-,hpk=3,mgx=1,vpf=7,pfdjc-,hc=7,hpk=6,dtf-,mbz-,kjxq=1,vd-,xj-,mclxh-,mxkr-,hs-,ckcf-,zgp-,rhs=2,bmtf=3,pnxx-,qcn=6,ltf=9,prz=4,nvzj-,pttv-,ms=9,cjj-,hpk-,nbp=7,fvq=1,mk=1,gnjn-,sfx=2,xl-,xxgf=1,knfmt-,dlf-,vhv-,xh-,xtv-,slhkm=1,tz-,xvj-,jb-,srl-,txpl=5,ksv-,dcb-,hbql=2,rqjm=1,llj-,jnmz=1,vlrft=8,fmvd-,vrd=4,km=2,ljq-,bhn=7,bpmqp-,krc-,dhj-,fsrk-,dd-,sm-,fd-,bpr=3,dpj-,jbt-,gj-,jrb=1,hphk-,xjs-,vg=8,qt-,rp-,fttd=3,krn-,jq-,gfhl=5,pbf-,slsv=8,llb-,cxqjcn-,jdn-,hphk=3,mtv=3,pgx-,qc-,zp-,mhj=1,mbz-,shmm-,qrv=6,mk=1,fh=9,rj-,slsv=8,tdqk=4,ndhfx=3,mn-,vx=3,nrf=3,jgxj-,qnl=5,jfpvgt=5,hbbsq-,rnj-,gdcv=9,fjg-,bmh-,kd=7,hgn-,mcm=3,hrppv=1,dc-,xs-,fv-,ml-,fqr=7,qn=9,dz-,tr=3,rkt=5,qcxq=7,hqmvs-,sl-,bbh=7,lr=5,prz-,rqkc=2,zgp-,zqqv=6,xbrg=1,bds=7,qbvx-,cfr-,dlf=8,zmqld-,hpk-,qqnx-,dtf-,thpc=8,mkqx-,zndpm=9,tdqk=4,fl-,kbp-,jrv-,ssq=1,llx-,qdx-,lrrt=4,rj=1,qj=2,fttd=5,pvb=3,ccn-,fsqpbs=7,pk=6,hdl=6,fttd=3,mt-,hprj=4,qd-,fk-,kx=9,ppd=2,phc-,vn-,hv-,xhj=3,ljq=8,prz-,lks=3,ccb=3,qt-,trjxdq-,mc-,hln=6,jqz=8,lc=4,zk=9,gvn-,qcn=6,brm=2,ccn=1,dh=6,dvm=9,cz=2,tvf-,dnfh=5,bf=6,ms-,bmb=6,fp-,slsv-,kfk=2,bs=8,hpk=1,hln-,hsv-,jbt=2,clrt=7,qdx-,lzg-,pbf=2,bf=4,gkkgm=2,fdkfc=6,kcvqv=8,dnfh=1,zpplm-,mgx=5,bp=9,rc-,tvf-,svj-,qt-,zp-,rkt-,dp-,kbp-,mf-,fmvd=3,dd-,lxdv-,hgn-,jng-,pqff=1,hp-,nqrdmh-,kphsqq-,pc-,lmfg=4,pv-,dq-,xc=8,xdl-,mmqm=6,ln-,mt-,kd=9,cxqlmd=9,jrv=4,jj=2,zqmhf=2,mtv=6,mj=4,qj=3,cbj-,fmf=7,cbslp-,bhn=3,ssq-,jfh-,rqkc-,zbp=9,qcxq-,sn=6,hdl=4,fl-,fd=3,mhj-,rmn-,bfl-,hphk-,fsqpbs=7,bvxnx-,dn-,dtxh=3,tb-,plh=5,xpj=8,mgx-,zqqv=8,zzp-,bxt=8,fsqpbs-,kjr-,pk-,cbj=4,dqz=1,bmb-,hcsbqm-,mr-,gdqpz-,rsnr=9,ttvr=1,hqmvs=7,fdkfc-,pmv-,qfxmp=8,xsg-,mjrl-,hn-,rxqbqv=8,bpr-,tt=7,kbp=5,gtms-,ssq-,tl=3,vcp=6,tl=6,kbp-,ssnbtj=1,zfb=5,dpfmm=7,kmgb=2,zngc-,ppxtq=8,qn=1,zzp=7,pk=6,fjg-,ph=5,fxnk=7,dkt-,qcn=2,cg-,dc-,gglrm=4,zzp-,htc=9,ptgp=7,vq=3,bpr=4,lbqn=2,zm-,rtnhrs-,fjg-,kpn-,cmsg-,dtsx=6,dkt=5,krp-,lxdv-,vv-,ksv=6,bmx-,kjr=7,cjj=9,rjz-,nhlmx=3,rp=4,hd=8,rzrx-,vlrft=9,bzxr-,kpn=4,hpk=3,mbz-,bxhr=8,ndhfx=6,kz-,kz=3,jrb=9,rjz-,dqz=8,sfx=9,qcn-,gkkgm-,txpl=9,mlh=5,qd-,df=1,njt=6,plh=7,zz=2,cbslp-,xj-,kdvhk-,qk=1,xbrg=4,ttvr-,zpplm=2,qd=6,nx-,qnl-,xxgf=5,dfzxj=5,rxlbkl=2,xxgf-,rc=7,dqz=9,bkc=9,bg=8,ms-,slxgsf=9,nrf=8,sr-,phpz-,dfxfb=5,fdkfc=2,ph=7,jfpvgt=6,lnl-,rqjm=9,mx=4,xhj-,bz=3,mfm-,tvf-,sl-,gj-,mjrl=5,vcp-,tf-,dkt-,hx-,xxgf=3,vvv-,mjq=1,mn-,xd=3,drc=2,jbt-,zndpm=1,npr-,ssnbtj=5,slxgsf-,vs=6,ms=3,phpz=8,dqz=6,xhj-,ln-,vlrft-,ksh=1,jnmz=3,hs-,krn=2,qvd-,vmhp=3,vg-,qhl=3,cvd=9,ttvr-,tp=7,rn=5,mkqx=8,zbq-,bmtf-,szqz-,vhsd-,jfh=9,kjxq-,bmtf-,mv-,dtsx=9,dd-,dtf-,sj-,pj-,xl=7,gdcv=9,mbz-,ll=9,dljx=8,gh=3,fg-,tdqk=7,bhn-,mxn=4,hzkxnp-,cstb-,vpm-,jq-,qm=2,sf-,jng-,pttv-,sf-,rjjg-,vq=5,rmn=8,pmv-,zpplm=3,bmb=7,ckk-,bpr=1,hbql-,vgvf=8,xjs=8,ml=8,lmfg-,hphk=6,gh=1,zp-,tx=9,jjxsf=3,pttv=2,mkxr=2,gv-,xhj=9,mbz=5,fv=2,pnxx=2,qp-,ppzjql-,svj-,lnl=4,pc-,hvh-,pt-,dlf=5,mlh=8,ckcf-,mzzg-,zfb-,kcvqv=6,jqz-,ml-,hvh-,bzxr-,vhv-,tl=1,dm-,hx=8,vrd-,hcsbqm-,rkt-,bf-,rmn-,fsqpbs-,chc-,kjr=6,jb-,dqrf-,mv-,pmz-,jjf-,qn-,vhd=7,fv=4,kd=5,mjrl=1,mkqx=6,tjfr=2,sf=3,xczgt=5,bq-,qd-,zmqld-,llb-,jgxj=9,gh-,tr=6,dkt=7,lx=4,qlf-,xvj=1,tf-,gdcv=2,bmx-,qdx=9,pfdjc=9,kj-,gdqpz=9,rqjm=3,zm=1,szqz=4,vd=4,mk-,xh-,lm-,xsg-,jfh-,vgvf-,mkxr-,smvsp=6,dc-,fmvd=3,ltf-,mbg-,lnl-,pjfrs=2,sh-,ksrg=6,bmb=2,pqff=9,gc=6,bzs-,vhv=5,rxqbqv=8,rhs-,vd=6,fmf-,qj=7,ts=1,xsg-,lmfg=9,kcvqv-,mhj=2,tt=2,vs=8,vhsd=1,rmn=1,dz-,qj-,ph-,hv-,rzrx-,lgt=7,jc-,cz-,xhj-,vv-,cg=5,gfhl-,pqff=4,lq=3,rp-,nx-,bbh=1,bq=9,ffr=5,ls=4,lq-,skrc=1,hdf=9,jqz=8,xj=4,zpplm-,jfpvgt=6,dnfh-,xgb-,qcn=8,jgxj=2,jnmz-,vlrft-,ml=3,hq=3,trdd=3,nkf-,fsqpbs-,qk-,mk-,sfx=5,nqrdmh-,hprj=7,xksq=3,rx-,qm-,fxrl=7,bxt-,vxpg=7,lr-,hcsbqm=8,qcn-,rp=2,vgt=6,dz-,kdvhk-,mcmmvv=4,fdkfc-,cz=6,dtf=2,ptgp=9,zz-,zgp-,gc=4,ksv-,qvd=3,rxqbqv-,xksq-,vn=8,gfj=5,dnfh-,nt=3,dljx=2,vs=5,dpfmm-,vx=8,vhsd=9,lx=6,xxgf-,rxlbkl=5,prz-,vpm=2,pbf=7,qk=8,vrd=9,gkkgm-,dk-,rcts=8,hq-,prz-,dp-,rx=2,fmvd-,hgn=1,fmf-,prz=2,qqnx=9,tjfr-,rrdkm=9,kd-,ssq=3,hphk=9,mf-,xl-,dvf=9,rqjhl-,ncz-,slsv-,ltf-,gnq=8,nkf-,nbb-,xgb-,rmn-,xd=8,ln=8,sr-,gfhl=7,lr-,fhgtq-,vpm-,sl=2,dhd=8,sfx-,gnjn-,mf-,lz=9,hs=5,chc=7,dq=2,prz=5,zzp=7,xhj=5,rrdkm=4,kbp=4,mhbk=6,nxc=5,ckk-,dd-,ffr-,xq=3,fvq-,bxhr=9,lbqn-,qg=1,gkr-,rxlbkl-,mjq-,knfmt=2,vvv=9,ndhfx=1,kjxq=6,mf=6,jfpvgt=3,zzp-,xxv=8,vv=3,ndhfx=4,xc=5,gglrm-,vxpg=7,ms=4,vjzc-,jmd-,fq=7,zqs-,pdkdj=4,lbqn-,vpf-,dlf=8,qpl=9,fl=2,tf=3,lklhn-,kd-,ljq-,nxh=9,pmz=6,xdzch-,bkc-,sd=8,dqrf=6,dlrz=4,qdv=1,bfl=4,mrt=8,zz-,tp-,qkbd=2,fsrk-,jjxsf-,xvj=1,rs=7,njt=2,vbbzrn=4,qc=9,gdfgc-,rhs=8,zcm-,vhsd-,fh-,fpvpht=9,bmb=5,shmm=4,nxh-,cxqjcn=8,hxq-,tp=4,mjrl-,gdfgc-,qp-,lc=9,gp=6,mzzg=5,svj=4,fp=6,htc-,rc=4,krn-,mclxh-,gnq=7,kcvqv=1,zxl=6,bxt-,slxgsf=6,ksv=8,dqrf=5,njt=2,qcn=5,qrv=9,srl-,dtsx-,lmfg=3,kzbr-,nkf-,qk=5,krp-,bzxr-,qdx=1,krn=8,sr-,fxnk-,vpx-,qms-,hbbsq-,lz-,hln-,cxqjcn-,dhj-,bkc=7,mfm=5,srl-,mn=3,qc-,dm=5,gvn=7,rx-,sd-,mcm=9,kj-,zgp-,dqz=5,xtv-,zz-,npr-,nkf=8,dvm-,spkk-,jgxj=1,smvsp=1,jz=7,pbf-,zpplm-,vd=6,rqjhl-,fsqpbs=6,thpc-,fdkfc=6,nhlmx=2,hs-,dfzxj-,dlrz-,dk=2,dlrz-,mv-,pjfrs=4,tp-,ccn-,pk-,ml=7,phr-,txpl-,slhkm-,dtsx=5,lbqn=3,ckcf=6,mbz=9,rqjhl=9,phr=9,kjkt=5,bcdsz-,dsv-,rqjm-";
        public void Solve()
        {
            var watch = Stopwatch.StartNew();
            var total = SolveA(input);
            Debug.WriteLine($"A) {total}");
            watch.Stop();
            Debug.WriteLine($"Elapsed {watch.ElapsedMilliseconds}ms");

            watch = Stopwatch.StartNew();
            SolveB(input);
            watch.Stop();
            Debug.WriteLine($"Elapsed {watch.ElapsedMilliseconds}ms");
        }

        int HashAlgorithm(string s) => s.Aggregate(0, (ch, a) => (ch + a) * 17 % 256);


        int SolveA(string input) => input.Split(',').Select(HashAlgorithm).Sum();

        void SolveB(string input)
        {
            Dictionary<int, List<ItemStringValue>> HASHMAP = new Dictionary<int, List<ItemStringValue>>();
            foreach(var part in input.Split(','))
            {
                if (part.Contains('='))
                {
                    var s = part.Split('=');
                    var h = HashAlgorithm(s[0]);
                    var newitem = new ItemStringValue(s[0], int.Parse(s[1]));

                    if (HASHMAP.ContainsKey(h))
                    {
                        var index = HASHMAP[h].FindIndex(item => item.stringValue == s[0]);
                        if ( index == -1)
                        {
                            HASHMAP[h].Add(newitem);
                        }
                        else
                        {
                            HASHMAP[h][index] = newitem;
                        }

                    }
                    else
                    {
                        HASHMAP.Add( h, new List<ItemStringValue> {  newitem } );
                    }                    
                }
                else
                {
                    var s = part.Split('-');
                    var h = HashAlgorithm(s[0]);
                    try{
                        HASHMAP[h].RemoveAll(item => item.stringValue == s[0]);
                    }catch(KeyNotFoundException){ }
                }                
            }

            var total = (from part in HASHMAP
                         from lensIndex in Enumerable.Range(0, part.Value.Count)
                         select (part.Key + 1) * (lensIndex + 1) * HASHMAP[part.Key][lensIndex].intValue).Sum();
            Debug.WriteLine($"B) {total}");
        }
    }
}
