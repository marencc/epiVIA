#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-10 14:45:36
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from Bio.Seq import Seq

ME_S7 = "CTGTCTCTTATACACATCTCCGAGCCCACGAGAC"
ME_S7_revc = str(Seq(ME_S7).reverse_complement())
S5_ME = "TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG"
S5_ME_revc = str(Seq(S5_ME).reverse_complement())

FRAGMENT_LEN = 1000		## set the maximun fragment length
VECTOR = 'pelps_cd19bbz' 	## Vector name
MIN_READS = 3

bb_conf = {
"geneHancerGenesTssAll.hg38":"./geneHancer/geneHancerGenesTssAll.hg38.bb",
"geneHancerRegElementsDoubleElite.hg38":"./geneHancer/geneHancerRegElementsDoubleElite.hg38.bb",
"geneHancerInteractionsAll.v2.hg38":"./geneHancer/geneHancerInteractionsAll.v2.hg38.bb",
"geneHancerRegElementsAll.hg38":"./geneHancer/geneHancerRegElementsAll.hg38.bb",
"geneHancerInteractionsDoubleElite.hg38":"./geneHancer/geneHancerInteractionsDoubleElite.hg38.bb",
"geneHancerGenesTssDoubleElite.hg38":"./geneHancer/geneHancerGenesTssDoubleElite.hg38.bb",
"geneHancerInteractionsDoubleElite.v2.hg38":"./geneHancer/geneHancerInteractionsDoubleElite.v2.hg38.bb",
"geneHancerInteractionsAll.hg38":"./geneHancer/geneHancerInteractionsAll.hg38.bb",
"unipSplice":"./uniprot/unipSplice.bb",
"unipLocCytopl":"./uniprot/unipLocCytopl.bb",
"unipModif":"./uniprot/unipModif.bb",
"unipChain":"./uniprot/unipChain.bb",
"unipConflict":"./uniprot/unipConflict.bb",
"unipOther":"./uniprot/unipOther.bb",
"unipLocExtra":"./uniprot/unipLocExtra.bb",
"unipDisulfBond":"./uniprot/unipDisulfBond.bb",
"unipDomain":"./uniprot/unipDomain.bb",
"unipMut":"./uniprot/unipMut.bb",
"unipAliTrembl":"./uniprot/unipAliTrembl.bb",
"unipRepeat":"./uniprot/unipRepeat.bb",
"unipStruct":"./uniprot/unipStruct.bb",
"unipAliSwissprot":"./uniprot/unipAliSwissprot.bb",
"unipLocSignal":"./uniprot/unipLocSignal.bb",
"unipLocTransMemb":"./uniprot/unipLocTransMemb.bb",
"crispr":"./crispr10K/crispr.bb",
"k50.Unique.Mappability":"./hoffmanMappability/k50.Unique.Mappability.bb",
"k36.G2A-Converted":"./hoffmanMappability/k36.G2A-Converted.bb",
"k24.Unique.Mappability":"./hoffmanMappability/k24.Unique.Mappability.bb",
"k36.Unique.Mappability":"./hoffmanMappability/k36.Unique.Mappability.bb",
"k24.G2A-Converted":"./hoffmanMappability/k24.G2A-Converted.bb",
"k100.G2A-Converted":"./hoffmanMappability/k100.G2A-Converted.bb",
"k24.C2T-Converted":"./hoffmanMappability/k24.C2T-Converted.bb",
"k50.C2T-Converted":"./hoffmanMappability/k50.C2T-Converted.bb",
"k50.G2A-Converted":"./hoffmanMappability/k50.G2A-Converted.bb",
"k100.Unique.Mappability":"./hoffmanMappability/k100.Unique.Mappability.bb",
"k36.C2T-Converted":"./hoffmanMappability/k36.C2T-Converted.bb",
"k100.C2T-Converted":"./hoffmanMappability/k100.C2T-Converted.bb",
"tcgaGeneExpr":"./tcga/tcgaGeneExpr.bb",
"tcgaTranscExpr":"./tcga/tcgaTranscExpr.bb",
"crispr":"./crispr/crispr.bb",
"knownGene29":"./knownGene29.bb",
"knownGene24":"./knownGene24.bb",
"mane.0.5":"./mane/mane.0.5.bb",
"miRnaAtlasSample1":"./bbi/miRnaAtlasSample1.bb",
"spAnnot":"./bbi/uniprot/spAnnot.bb",
"spMut":"./bbi/uniprot/spMut.bb",
"spStruct":"./bbi/uniprot/spStruct.bb",
"miRnaAtlasSample2":"./bbi/miRnaAtlasSample2.bb",
"wgEncodeRegDnaseUwJurkatHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwJurkatHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwBjHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwBjHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwTh1Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwTh1Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHreHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHreHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwLhcnm2Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwLhcnm2Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHcpepicHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHcpepicHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwNt2d1Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwNt2d1Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHgfHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHgfHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmvecdblneoHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmvecdblneoHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHvmfHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHvmfHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwT47dHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwT47dHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHct116Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHct116Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwRptecHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwRptecHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHsmmHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHsmmHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHbmecHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHbmecHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHaepicHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHaepicHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHrpepicHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHrpepicHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwMcf7Estradiolctrl0hrHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwMcf7Estradiolctrl0hrHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwMonocytescd14ro01746Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwMonocytescd14ro01746Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwNhdfadHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwNhdfadHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwGm12878Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwGm12878Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwAg10803Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwAg10803Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHipepicHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHipepicHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwPanc1Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwPanc1Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmfHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmfHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwNhdfneoHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwNhdfneoHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwM059jHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwM059jHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwH7hescDiffprota14dHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwH7hescDiffprota14dHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwSkmcHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwSkmcHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHbvsmcHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHbvsmcHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwAg09309Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwAg09309Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHrcepicHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHrcepicHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHrgecHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHrgecHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHuvecHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHuvecHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwGm04503Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwGm04503Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwRpmi7951Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwRpmi7951Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwCaco2Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwCaco2Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwGm04504Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwGm04504Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwLncapHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwLncapHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwMcf7Estradiol100nm1hrHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwMcf7Estradiol100nm1hrHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHelas3Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHelas3Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHpfHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHpfHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwMcf7Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwMcf7Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwNhlfHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwNhlfHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwNb4Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwNb4Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHeepicHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHeepicHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwSaecHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwSaecHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHsmmtubeHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHsmmtubeHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwNhaHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwNhaHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHahHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHahHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwTh2Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwTh2Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwNhberaHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwNhberaHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwAg04450Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwAg04450Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwSknmcHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwSknmcHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHffmycHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHffmycHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwBonemarrowmscHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwBonemarrowmscHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHcfHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHcfHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwCd20ro01778Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwCd20ro01778Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmveclblHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmveclblHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwPrecHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwPrecHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwGm06990Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwGm06990Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmecHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmecHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwK562Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwK562Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwAoafHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwAoafHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHpafHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHpafHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwAg09319Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwAg09319Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmvecdbladHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmvecdbladHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmvecdlyadHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmvecdlyadHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHconfHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHconfHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwLhcnm2Diff4dHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwLhcnm2Diff4dHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmvecdlyneoHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmvecdlyneoHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwH7hescDiffprota5dHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwH7hescDiffprota5dHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmvecllyHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmvecllyHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHcfaaHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHcfaaHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwWerirb1Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwWerirb1Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHcmHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHcmHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmvecdadHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmvecdadHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHffHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHffHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHepg2Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHepg2Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwGm12865Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwGm12865Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHmvecdneoHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHmvecdneoHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHaspHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHaspHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHpdlfHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHpdlfHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwA549Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwA549Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwTh1wb54553204Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwTh1wb54553204Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwAg04449Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwAg04449Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHacHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHacHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwWi38Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwWi38Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwSknshraHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwSknshraHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHnpcepicHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHnpcepicHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwH7hescHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwH7hescHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwNhekHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwNhekHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwHl60Hotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwHl60Hotspot.broadPeak.bb",
"wgEncodeRegDnaseUwBe2cHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwBe2cHotspot.broadPeak.bb",
"wgEncodeRegDnaseUwWi384ohtam20nm72hrHotspot.broadPeak":"./bbi/wgEncodeRegDnase/wgEncodeRegDnaseUwWi384ohtam20nm72hrHotspot.broadPeak.bb",
"hg38.grcIncidentDb":"./bbi/grcIncidentDb/hg38.grcIncidentDb.bb",
"snpediaAll":"./bbi/snpediaAll.bb",
"lrg":"./bbi/lrg.bb",
"hgmd":"./bbi/hgmd.bb",
"interactions":"./bbi/interactions.bb",
"clinvarMain":"./bbi/clinvar/clinvarMain.bb",
"clinvarCnv":"./bbi/clinvar/clinvarCnv.bb",
"lrg":"./bbi/lrgRegions/lrg.bb",
"knownGene":"./knownGene.bb",
"ncbiRefSeqGenomicDiff":"./ncbiRefSeq/ncbiRefSeqGenomicDiff.bb",
"ncbiRefSeqOther":"./ncbiRefSeq/ncbiRefSeqOther.bb",
"refSeqFuncElems":"./ncbiRefSeq/refSeqFuncElems.bb",
"snp150.bed4":"./vai/snp150.bed4.bb",
"snp147.bed4":"./vai/snp147.bed4.bb",
"snp151.bed4":"./vai/snp151.bed4.bb",
"dbNsfpUniProt":"./dbNsfp/dbNsfpUniProt.bb",
"dbNsfpMutationAssessor":"./dbNsfp/dbNsfpMutationAssessor.bb",
"dbNsfpSeqChange":"./dbNsfp/dbNsfpSeqChange.bb",
"dbNsfpPolyPhen2":"./dbNsfp/dbNsfpPolyPhen2.bb",
"dbNsfpLrt":"./dbNsfp/dbNsfpLrt.bb",
"dbNsfpMutationTaster":"./dbNsfp/dbNsfpMutationTaster.bb",
"dbNsfpVest":"./dbNsfp/dbNsfpVest.bb",
"dbNsfpSift":"./dbNsfp/dbNsfpSift.bb",
"dbNsfpInterPro":"./dbNsfp/dbNsfpInterPro.bb",
"gtexTranscExpr":"./gtex/gtexTranscExpr.bb",
}