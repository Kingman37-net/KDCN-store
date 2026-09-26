/* =========================================================
   KDCN SERVICE CATALOGUE — Master Data
   Tiers: Essential | Professional | Business | Advanced
   ========================================================= */

const KDCN_TIERS = [
  {
    id: "essential",
    name: "Essential Digital Services",
    icon: "🟢",
    tagline: "Quick digital assistance for everyday needs",
    description: "For individuals who need a specific digital task, document, online service, or quick technical assistance.",
    idealFor: "Individuals, students, job seekers and personal users",
    priceRange: "From KES 250",
    color: "#22c55e"
  },
  {
    id: "professional",
    name: "Professional Digital Services",
    icon: "🟡",
    tagline: "Build a stronger professional presence",
    description: "For clients who want to establish a stronger professional presence, improve their career position, or build a reliable digital foundation.",
    idealFor: "Professionals, entrepreneurs, startups and SMEs",
    priceRange: "KES 1,500 – 7,299",
    color: "#fbbf24"
  },
  {
    id: "business",
    name: "Business & Growth Solutions",
    icon: "🔵",
    tagline: "Integrated digital services for growing organizations",
    description: "For businesses and organizations that require integrated digital services, stronger online visibility, or ongoing management and support.",
    idealFor: "Growing businesses, brands, organizations and established service providers",
    priceRange: "KES 12,000 – 17,499",
    color: "#00d1ff"
  },
  {
    id: "advanced",
    name: "Advanced Digital Solutions",
    icon: "🟣",
    tagline: "Comprehensive development and technology",
    description: "For clients requiring comprehensive website development, branding, technology implementation and customized digital solutions.",
    idealFor: "Established businesses, organizations, NGOs, corporates and larger digital projects",
    priceRange: "KES 19,999 – 40,000",
    color: "#a855f7"
  }
];

const KDCN_SERVICES = [
  /* =========================================================
     🟢 ESSENTIAL DIGITAL SERVICES
     ========================================================= */
  {
    id: "online-cyber-services",
    code: "KDCNPACKAGE001",
    tier: "essential",
    name: "Online Cyber & Digital Services",
    tagline: "Fast access to essential online, government and digital services.",
    fee: "From KES 250",
    feeMin: 250,
    idealFor: "Individuals, students and job seekers",
    objective: "Fast and convenient access to essential online, government and digital services.",
    includes: [
      "eCitizen phone number and email updates",
      "KRA email updates",
      "KRA PIN retrieval and new application",
      "KRA return filing",
      "KRA group PIN applications and approvals",
      "KRA group PIN retrieval",
      "SHA registration and related services",
      "SHA dependant and number updates",
      "Name updates on eCitizen",
      "Certificate of Good Conduct application",
      "Birth certificate applications",
      "Vehicle class endorsement services",
      "Passport application and replacement assistance",
      "Driving licence renewal services",
      "Smart Driving Licence renewal assistance",
      "Archived driving licence assistance",
      "NSSF registration and number retrieval",
      "ID validation assistance through IPRS",
      "HELB loan application and clearance certificate assistance",
      "NCK licence renewal and examination-related services",
      "TSC-related online services",
      "CV and cover letter typing and updating",
      "Computer certificate services",
      "Document formatting and conversion",
      "Computer skills training",
      "Online computer training",
      "Job search and application assistance"
    ],
    image: "assets/services/online-cyber-services.png",
    whatsapp: "Hi KDCN, I'm interested in Online Cyber & Digital Services (from KES 250). Please share details."
  },
  {
    id: "poster-flyer-design",
    code: "KDCNPACKAGE002",
    tier: "essential",
    name: "Poster & Flyer Design",
    tagline: "Professional visual materials that attract attention.",
    fee: "From KES 500",
    feeMin: 500,
    idealFor: "Event organizers, businesses, individuals and organizations",
    objective: "Create professional visual materials designed to communicate clearly and attract attention.",
    includes: [
      "Custom poster or flyer design",
      "A4 and social-media formats",
      "Up to 2 revision rounds",
      "Print-ready PDF/PNG files",
      "Standard turnaround: 24–48 hours"
    ],
    image: "assets/services/poster-flyer-design.jpg",
    whatsapp: "Hi KDCN, I'd like a Poster & Flyer Design quote (from KES 500). Here's my project: "
  },
  {
    id: "business-email-setup",
    code: "KDCNPACKAGE003",
    tier: "essential",
    name: "Business Email Setup",
    tagline: "Look professional with branded email.",
    fee: "KES 1,000",
    feeMin: 1000,
    idealFor: "Businesses with an existing domain name",
    objective: "Establish a professional business email system using your own domain.",
    includes: [
      "Professional email address, e.g. info@yourbusiness.com",
      "Setup on Gmail, Outlook and/or mobile devices",
      "SPF and DKIM configuration",
      "Basic email delivery configuration",
      "Up to 1 year of setup support"
    ],
    image: "assets/services/business-email-setup.png",
    whatsapp: "Hi KDCN, I need Business Email Setup (KES 1,000). My domain is: "
  },

  /* =========================================================
     🟡 PROFESSIONAL DIGITAL SERVICES
     ========================================================= */
  {
    id: "cv-cover-letter",
    code: "KDCNPACKAGE004",
    tier: "professional",
    name: "CV & Cover Letter Package",
    tagline: "Present your qualifications professionally.",
    fee: "From KES 1,500",
    feeMin: 1500,
    idealFor: "Job seekers, graduates and professionals",
    objective: "Present your qualifications in a professional, structured and application-ready format.",
    includes: [
      "Professional CV development",
      "ATS-friendly formatting",
      "Tailored cover letter",
      "LinkedIn profile optimization",
      "Editable Word document",
      "Final PDF version"
    ],
    image: "assets/services/cv-cover-letter.png",
    whatsapp: "Hi KDCN, I want the CV & Cover Letter Package (from KES 1,500). My target role is: "
  },
  {
    id: "google-business-profile",
    code: "KDCNPACKAGE005",
    tier: "professional",
    name: "Google Business Profile Setup",
    tagline: "Get found on Google Search and Google Maps.",
    fee: "KES 1,500",
    feeMin: 1500,
    idealFor: "Local businesses, shops and service providers",
    objective: "Improve your visibility across Google Search and Google Maps.",
    includes: [
      "Google Business Profile creation or claim assistance",
      "Business information optimization",
      "Photos, hours and service configuration",
      "Category and profile optimization",
      "Local visibility guidance",
      "Verification assistance (subject to Google's requirements)"
    ],
    image: "assets/services/google-my-business.png",
    whatsapp: "Hi KDCN, I need Google Business Profile Setup (KES 1,500). My business: "
  },
  {
    id: "starter-digital-access",
    code: "KDCNPACKAGE006",
    tier: "professional",
    name: "Starter Digital Access Package",
    tagline: "Essential digital, government and document services.",
    fee: "KES 1,500",
    feeMin: 1500,
    idealFor: "Individuals, students and job seekers",
    objective: "Provide convenient access to essential digital, government and document services.",
    includes: [
      "eCitizen and basic government service assistance",
      "KRA PIN application, retrieval and updates",
      "SHA and NSSF services",
      "Document typing and formatting",
      "Job application support",
      "General online assistance"
    ],
    image: "assets/services/starter-digital-access.png",
    whatsapp: "Hi KDCN, I'm interested in the Starter Digital Access Package (KES 1,500)."
  },
  {
    id: "digital-strategy-consultation",
    code: "KDCNPACKAGE007",
    tier: "professional",
    name: "Digital Strategy Consultation",
    tagline: "Identify your digital position and plan growth.",
    fee: "KES 1,500 per session",
    feeMin: 1500,
    idealFor: "Entrepreneurs and business owners",
    objective: "Identify your current digital position and establish a practical roadmap for growth.",
    includes: [
      "1-hour one-on-one consultation",
      "Video or voice session",
      "Digital presence assessment",
      "Opportunity and gap review",
      "Practical action plan",
      "Follow-up summary in PDF format"
    ],
    image: "assets/services/digital-strategy-consultation.png",
    whatsapp: "Hi KDCN, I'd like a Digital Strategy Consultation (KES 1,500). My business: "
  },
  {
    id: "professional-career",
    code: "KDCNPACKAGE008",
    tier: "professional",
    name: "Professional Career Package",
    tagline: "Complete career support from preparation to submission.",
    fee: "KES 3,000",
    feeMin: 3000,
    idealFor: "Job seekers and professionals",
    objective: "Provide practical career and digital application support from preparation through submission.",
    includes: [
      "CV and cover letter development",
      "Job application assistance",
      "Application tracking support",
      "Good Conduct application assistance",
      "Academic, KUCCPS and HELB support",
      "Document conversion and formatting"
    ],
    image: "assets/services/professional-career.png",
    whatsapp: "Hi KDCN, I want the Professional Career Package (KES 3,000)."
  },
  {
    id: "logo-branding",
    code: "KDCNPACKAGE009",
    tier: "professional",
    name: "Logo & Branding Package",
    tagline: "Establish a consistent visual identity.",
    fee: "From KES 3,000",
    feeMin: 3000,
    idealFor: "Startups, SMEs and businesses undergoing rebranding",
    objective: "Establish a consistent and recognizable visual identity.",
    includes: [
      "Up to 3 initial logo concepts",
      "Up to 2 revision rounds",
      "High-resolution PNG, JPG and PDF files",
      "Brand colour palette recommendation",
      "Basic visual branding direction"
    ],
    image: "assets/services/logo-branding.jpg",
    whatsapp: "Hi KDCN, I need the Logo & Branding Package (from KES 3,000). My business: "
  },
  {
    id: "business-startup",
    code: "KDCNPACKAGE010",
    tier: "professional",
    name: "Business Startup Package",
    tagline: "Launch your business with a professional foundation.",
    fee: "KES 5,000",
    feeMin: 5000,
    idealFor: "Startups, SMEs and entrepreneurs",
    objective: "Support the initial business setup and establish a professional foundation.",
    includes: [
      "Business name registration assistance",
      "Company profile",
      "Articles of Association support",
      "KRA PIN assistance",
      "Basic branding guidance"
    ],
    image: "assets/services/business-startup.png",
    whatsapp: "Hi KDCN, I want the Business Startup Package (KES 5,000)."
  },
  {
    id: "social-media-management",
    code: "KDCNPACKAGE011",
    tier: "professional",
    name: "Social Media Management",
    tagline: "Build a consistent social media presence.",
    fee: "From KES 5,000/month",
    feeMin: 5000,
    idealFor: "Businesses, brands and public-facing professionals",
    objective: "Build a consistent social media presence through structured content and account management.",
    includes: [
      "Content creation",
      "Posts, stories and short-form video content",
      "Hashtag and content strategy",
      "Audience engagement support",
      "Monthly performance reporting",
      "Platform support for Facebook, Instagram, TikTok and LinkedIn"
    ],
    image: "assets/services/social-media-management.jpg",
    whatsapp: "Hi KDCN, I'm interested in Social Media Management (from KES 5,000/month)."
  },

  /* =========================================================
     🔵 BUSINESS & GROWTH SOLUTIONS
     ========================================================= */
  {
    id: "website-design",
    code: "KDCNPACKAGE012",
    tier: "business",
    name: "Website Design Package",
    tagline: "Professional, responsive and accessible online presence.",
    fee: "From KES 15,000",
    feeMin: 15000,
    idealFor: "Small businesses, startups and organizations",
    objective: "Establish a professional, responsive and accessible online presence.",
    includes: [
      "Custom website design",
      "Mobile-responsive layout",
      "Up to 5 standard pages",
      "Home, About, Services, Contact and Blog structure",
      "Basic SEO configuration",
      "Contact form",
      "Social media integration"
    ],
    image: "assets/services/website-design.jpg",
    whatsapp: "Hi KDCN, I need the Website Design Package (from KES 15,000)."
  },
  {
    id: "cross-platform-growth",
    code: "KDCNPACKAGE013",
    tier: "business",
    name: "Cross-Platform Growth Bundle",
    tagline: "Coordinated presence across multiple social platforms.",
    fee: "KES 12,000",
    feeMin: 12000,
    idealFor: "Businesses, brands and creators",
    objective: "Establish a coordinated presence across multiple social platforms.",
    includes: [
      "Instagram management",
      "Facebook management",
      "TikTok management",
      "YouTube support",
      "X management",
      "Profile optimization",
      "Content strategy",
      "Hashtag research",
      "Engagement support",
      "Growth monitoring",
      "Monthly performance reporting"
    ],
    image: "assets/services/cross-platform-growth.png",
    whatsapp: "Hi KDCN, I want the Cross-Platform Growth Bundle (KES 12,000)."
  },

  /* =========================================================
     🟣 ADVANCED DIGITAL SOLUTIONS
     ========================================================= */
  {
    id: "website-launch",
    code: "KDCNPACKAGE014",
    tier: "advanced",
    name: "Website Launch Offer",
    tagline: "Launch a professional website with essential infrastructure.",
    fee: "KES 19,999",
    feeMin: 19999,
    badge: "LIMITED OFFER",
    idealFor: "Small businesses, startups and personal brands",
    objective: "Launch a professional website with the essential infrastructure required for online operations.",
    includes: [
      "2-page website structure",
      "Responsive and mobile-optimized design",
      "1 year of hosting",
      "Domain name",
      "Business email accounts",
      "Contact form",
      "Speed optimization",
      "Social media integration"
    ],
    image: "assets/services/website-promo.png",
    whatsapp: "Hi KDCN, I'm interested in the Website Launch Offer (KES 19,999)."
  },
  {
    id: "business-digital-presence",
    code: "KDCNPACKAGE015",
    tier: "advanced",
    name: "Business Digital Presence Package",
    tagline: "Unified and professional digital identity.",
    fee: "KES 20,000",
    feeMin: 20000,
    idealFor: "Growing businesses",
    objective: "Establish a unified and professional digital identity across key business channels.",
    includes: [
      "Professional website",
      "Logo design",
      "Business email setup",
      "WhatsApp Business optimization",
      "Basic digital branding",
      "Core online presence configuration"
    ],
    image: "assets/services/business-digital-presence.png",
    whatsapp: "Hi KDCN, I want the Business Digital Presence Package (KES 20,000)."
  },
  {
    id: "premium-brand-tech",
    code: "KDCNPACKAGE016",
    tier: "advanced",
    name: "Premium Brand & Technology Package",
    tagline: "Comprehensive digital identity with professional infrastructure.",
    fee: "KES 35,000",
    feeMin: 35000,
    idealFor: "Established businesses, NGOs, organizations and brands",
    objective: "Build a comprehensive digital identity supported by professional technology infrastructure.",
    includes: [
      "Advanced website development",
      "Professional logo and brand identity",
      "Designed company profile",
      "Domain and hosting setup",
      "Initial technical support",
      "Up to 30 days of post-delivery support"
    ],
    image: "assets/services/premium-brand-tech.png",
    whatsapp: "Hi KDCN, I'm interested in the Premium Brand & Technology Package (KES 35,000)."
  }
];

/* =========================================================
   HELPERS
   ========================================================= */
function getServiceById(id) {
  return KDCN_SERVICES.find(s => s.id === id);
}

function getServicesByTier(tier) {
  return KDCN_SERVICES.filter(s => s.tier === tier);
}

function getAllServices() {
  return KDCN_SERVICES;
}

function getTierById(id) {
  return KDCN_TIERS.find(t => t.id === id);
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { KDCN_SERVICES, KDCN_TIERS, getServiceById, getServicesByTier, getAllServices, getTierById };
}
