<?php

namespace Lib\Enum;

/**
 * Class CountryEnum
 * @package Lib\Enum
 */
class CountryEnum extends AbstractEnum
{
    public const
        AF = 'af',
        AL = 'al',
        DZ = 'dz',
        AD = 'ad',
        AO = 'ao',
        AG = 'ag',
        AR = 'ar',
        AM = 'am',
        AU = 'au',
        AT = 'at',
        AZ = 'az',
        BS = 'bs',
        BH = 'bh',
        BD = 'bd',
        BB = 'bb',
        BY = 'by',
        BE = 'be',
        BZ = 'bz',
        BJ = 'bj',
        BT = 'bt',
        BO = 'bo',
        BA = 'ba',
        BW = 'bw',
        BR = 'br',
        BN = 'bn',
        BG = 'bg',
        BF = 'bf',
        BI = 'bi',
        CI = 'ci',
        CV = 'cv',
        KH = 'kh',
        CM = 'cm',
        CA = 'ca',
        CF = 'cf',
        TD = 'td',
        CL = 'cl',
        CN = 'cn',
        CO = 'co',
        KM = 'km',
        CR = 'cr',
        HR = 'hr',
        CU = 'cu',
        CY = 'cy',
        CZ = 'cz',
        CD = 'cd',
        DK = 'dk',
        DJ = 'dj',
        DM = 'dm',
        DO = 'do',
        EC = 'ec',
        EG = 'eg',
        SV = 'sv',
        GQ = 'gq',
        ER = 'er',
        EE = 'ee',
        SZ = 'sz',
        ET = 'et',
        FJ = 'fj',
        FI = 'fi',
        FR = 'fr',
        GA = 'ga',
        GM = 'gm',
        GE = 'ge',
        DE = 'de',
        GH = 'gh',
        GR = 'gr',
        GD = 'gd',
        GT = 'gt',
        GN = 'gn',
        GW = 'gw',
        GF = 'gf',
        HT = 'ht',
        VA = 'va',
        HN = 'hn',
        HU = 'hu',
        IS = 'is',
        IN = 'in',
        ID = 'id',
        IR = 'ir',
        IQ = 'iq',
        IE = 'ie',
        IL = 'il',
        IT = 'it',
        JM = 'jm',
        JP = 'jp',
        JO = 'jo',
        KZ = 'kz',
        KE = 'ke',
        KI = 'ki',
        KW = 'kw',
        KG = 'kg',
        LA = 'la',
        LV = 'lv',
        LB = 'lb',
        LS = 'ls',
        LR = 'lr',
        LY = 'ly',
        LI = 'li',
        LT = 'lt',
        LU = 'lu',
        MG = 'mg',
        MW = 'mw',
        MY = 'my',
        MV = 'mv',
        ML = 'ml',
        MT = 'mt',
        MH = 'mh',
        MR = 'mr',
        MU = 'mu',
        MX = 'mx',
        FM = 'fm',
        MD = 'md',
        MC = 'mc',
        MN = 'mn',
        ME = 'me',
        MA = 'ma',
        MZ = 'mz',
        MM = 'mm',
        NA = 'na',
        NR = 'nr',
        NP = 'np',
        NL = 'nl',
        NZ = 'nz',
        NI = 'ni',
        NE = 'ne',
        NG = 'ng',
        KP = 'kp',
        MK = 'mk',
        NO = 'no',
        OM = 'om',
        PK = 'pk',
        PW = 'pw',
        PS = 'ps',
        PA = 'pa',
        PG = 'pg',
        PY = 'py',
        PE = 'pe',
        PH = 'ph',
        PL = 'pl',
        PT = 'pt',
        QA = 'qa',
        RO = 'ro',
        RU = 'ru',
        RW = 'rw',
        KN = 'kn',
        LC = 'lc',
        VC = 'vc',
        WS = 'ws',
        SM = 'sm',
        ST = 'st',
        SA = 'sa',
        SN = 'sn',
        RS = 'rs',
        SC = 'sc',
        SL = 'sl',
        SG = 'sg',
        SK = 'sk',
        SI = 'si',
        SB = 'sb',
        SO = 'so',
        ZA = 'za',
        KR = 'kr',
        SS = 'ss',
        ES = 'es',
        LK = 'lk',
        SD = 'sd',
        SR = 'sr',
        SE = 'se',
        CH = 'ch',
        SY = 'sy',
        TJ = 'tj',
        TZ = 'tz',
        TH = 'th',
        TL = 'tl',
        TG = 'tg',
        TO = 'to',
        TT = 'tt',
        TN = 'tn',
        TR = 'tr',
        TM = 'tm',
        TV = 'tv',
        UG = 'ug',
        UA = 'ua',
        AE = 'ae',
        GB = 'gb',
        US = 'us',
        UY = 'uy',
        UZ = 'uz',
        VU = 'vu',
        VE = 've',
        VN = 'vn',
        YE = 'ye',
        ZM = 'zm',
        ZW = 'zw'
    ;

    public static function getTitle(string $str): string
    {
        switch ($str) {
            case self::AF:
                return 'Afghanistan';
            case self::AL:
                return 'Albania';
            case self::DZ:
                return 'Algeria';
            case self::AD:
                return 'Andorra';
            case self::AO:
                return 'Angola';
            case self::AG:
                return 'Antigua and barbuda';
            case self::AR:
                return 'Argentina';
            case self::AM:
                return 'Armenia';
            case self::AU:
                return 'Australia';
            case self::AT:
                return 'Austria';
            case self::AZ:
                return 'Azerbaijan';
            case self::BS:
                return 'Bahamas';
            case self::BH:
                return 'Bahrain';
            case self::BD:
                return 'Bangladesh';
            case self::BB:
                return 'Barbados';
            case self::BY:
                return 'Belarus';
            case self::BE:
                return 'Belgium';
            case self::BZ:
                return 'Belize';
            case self::BJ:
                return 'Benin';
            case self::BT:
                return 'Bhutan';
            case self::BO:
                return 'Bolivia';
            case self::BA:
                return 'Bosnia and herzegovina';
            case self::BW:
                return 'Botswana';
            case self::BR:
                return 'Brazil';
            case self::BN:
                return 'Brunei';
            case self::BG:
                return 'Bulgaria';
            case self::BF:
                return 'Burkina faso';
            case self::BI:
                return 'Burundi';
            case self::CI:
                return 'Cote divoire';
            case self::CV:
                return 'Cabo verde';
            case self::KH:
                return 'Cambodia';
            case self::CM:
                return 'Cameroon';
            case self::CA:
                return 'Canada';
            case self::CF:
                return 'Central african republic';
            case self::TD:
                return 'Chad';
            case self::CL:
                return 'Chile';
            case self::CN:
                return 'China';
            case self::CO:
                return 'Colombia';
            case self::KM:
                return 'Comoros';
            case self::CR:
                return 'Costa rica';
            case self::HR:
                return 'Croatia';
            case self::CU:
                return 'Cuba';
            case self::CY:
                return 'Cyprus';
            case self::CZ:
                return 'Czechia';
            case self::CD:
                return 'Democratic republic of the congo';
            case self::DK:
                return 'Denmark';
            case self::DJ:
                return 'Djibouti';
            case self::DM:
                return 'Dominica';
            case self::DO:
                return 'Dominican republic';
            case self::EC:
                return 'Ecuador';
            case self::EG:
                return 'Egypt';
            case self::SV:
                return 'El salvador';
            case self::GQ:
                return 'Equatorial guinea';
            case self::ER:
                return 'Eritrea';
            case self::EE:
                return 'Estonia';
            case self::SZ:
                return 'Eswatini';
            case self::ET:
                return 'Ethiopia';
            case self::FJ:
                return 'Fiji';
            case self::FI:
                return 'Finland';
            case self::FR:
                return 'France';
            case self::GA:
                return 'Gabon';
            case self::GM:
                return 'Gambia';
            case self::GE:
                return 'Georgia';
            case self::DE:
                return 'Germany';
            case self::GH:
                return 'Ghana';
            case self::GR:
                return 'Greece';
            case self::GD:
                return 'Grenada';
            case self::GT:
                return 'Guatemala';
            case self::GN:
                return 'Guinea';
            case self::GW:
                return 'Guinea bissau';
            case self::GF:
                return 'Guyana';
            case self::HT:
                return 'Haiti';
            case self::VA:
                return 'Holy see';
            case self::HN:
                return 'Honduras';
            case self::HU:
                return 'Hungary';
            case self::IS:
                return 'Iceland';
            case self::IN:
                return 'India';
            case self::ID:
                return 'Indonesia';
            case self::IR:
                return 'Iran';
            case self::IQ:
                return 'Iraq';
            case self::IE:
                return 'Ireland';
            case self::IL:
                return 'Israel';
            case self::IT:
                return 'Italy';
            case self::JM:
                return 'Jamaica';
            case self::JP:
                return 'Japan';
            case self::JO:
                return 'Jordan';
            case self::KZ:
                return 'Kazakhstan';
            case self::KE:
                return 'Kenya';
            case self::KI:
                return 'Kiribati';
            case self::KW:
                return 'Kuwait';
            case self::KG:
                return 'Kyrgyzstan';
            case self::LA:
                return 'Laos';
            case self::LV:
                return 'Latvia';
            case self::LB:
                return 'Lebanon';
            case self::LS:
                return 'Lesotho';
            case self::LR:
                return 'Liberia';
            case self::LY:
                return 'Libya';
            case self::LI:
                return 'Liechtenstein';
            case self::LT:
                return 'Lithuania';
            case self::LU:
                return 'Luxembourg';
            case self::MG:
                return 'Madagascar';
            case self::MW:
                return 'Malawi';
            case self::MY:
                return 'Malaysia';
            case self::MV:
                return 'Maldives';
            case self::ML:
                return 'Mali';
            case self::MT:
                return 'Malta';
            case self::MH:
                return 'Marshall islands';
            case self::MR:
                return 'Mauritania';
            case self::MU:
                return 'Mauritius';
            case self::MX:
                return 'Mexico';
            case self::FM:
                return 'Micronesia';
            case self::MD:
                return 'Moldova';
            case self::MC:
                return 'Monaco';
            case self::MN:
                return 'Mongolia';
            case self::ME:
                return 'Montenegro';
            case self::MA:
                return 'Morocco';
            case self::MZ:
                return 'Mozambique';
            case self::MM:
                return 'Myanmar';
            case self::NA:
                return 'Namibia';
            case self::NR:
                return 'Nauru';
            case self::NP:
                return 'Nepal';
            case self::NL:
                return 'Netherlands';
            case self::NZ:
                return 'New zealand';
            case self::NI:
                return 'Nicaragua';
            case self::NE:
                return 'Niger';
            case self::NG:
                return 'Nigeria';
            case self::KP:
                return 'North korea';
            case self::MK:
                return 'North macedonia';
            case self::NO:
                return 'Norway';
            case self::OM:
                return 'Oman';
            case self::PK:
                return 'Pakistan';
            case self::PW:
                return 'Palau';
            case self::PS:
                return 'Palestine state';
            case self::PA:
                return 'Panama';
            case self::PG:
                return 'Papua new guinea';
            case self::PY:
                return 'Paraguay';
            case self::PE:
                return 'Peru';
            case self::PH:
                return 'Philippines';
            case self::PL:
                return 'Poland';
            case self::PT:
                return 'Portugal';
            case self::QA:
                return 'Qatar';
            case self::RO:
                return 'Romania';
            case self::RU:
                return 'Russia';
            case self::RW:
                return 'Rwanda';
            case self::KN:
                return 'Saint kitts and nevis';
            case self::LC:
                return 'Saint lucia';
            case self::VC:
                return 'Saint vincent and the grenadines';
            case self::WS:
                return 'Samoa';
            case self::SM:
                return 'San marino';
            case self::ST:
                return 'Sao tome and principe';
            case self::SA:
                return 'Saudi arabia';
            case self::SN:
                return 'Senegal';
            case self::RS:
                return 'Serbia';
            case self::SC:
                return 'Seychelles';
            case self::SL:
                return 'Sierra leone';
            case self::SG:
                return 'Singapore';
            case self::SK:
                return 'Slovakia';
            case self::SI:
                return 'Slovenia';
            case self::SB:
                return 'Solomon islands';
            case self::SO:
                return 'Somalia';
            case self::ZA:
                return 'South africa';
            case self::KR:
                return 'South korea';
            case self::SS:
                return 'South sudan';
            case self::ES:
                return 'Spain';
            case self::LK:
                return 'Sri lanka';
            case self::SD:
                return 'Sudan';
            case self::SR:
                return 'Suriname';
            case self::SE:
                return 'Sweden';
            case self::CH:
                return 'Switzerland';
            case self::SY:
                return 'Syria';
            case self::TJ:
                return 'Tajikistan';
            case self::TZ:
                return 'Tanzania';
            case self::TH:
                return 'Thailand';
            case self::TL:
                return 'Timor leste';
            case self::TG:
                return 'Togo';
            case self::TO:
                return 'Tonga';
            case self::TT:
                return 'Trinidad and tobago';
            case self::TN:
                return 'Tunisia';
            case self::TR:
                return 'Turkey';
            case self::TM:
                return 'Turkmenistan';
            case self::TV:
                return 'Tuvalu';
            case self::UG:
                return 'Uganda';
            case self::UA:
                return 'Ukraine';
            case self::AE:
                return 'United arab emirates';
            case self::GB:
                return 'United kingdom';
            case self::US:
                return 'United states of america';
            case self::UY:
                return 'Uruguay';
            case self::UZ:
                return 'Uzbekistan';
            case self::VU:
                return 'Vanuatu';
            case self::VE:
                return 'Venezuela';
            case self::VN:
                return 'Vietnam';
            case self::YE:
                return 'Yemen';
            case self::ZM:
                return 'Zambia';
            case self::ZW:
                return 'Zimbabwe';
            default:
                return parent::getTitle($str);
        }
    }
}
