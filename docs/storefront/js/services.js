/* =========================================================
   KDCN SERVICE CATALOG — Single Source of Truth
   ========================================================= */

const KDCN_SERVICES = [
  // ==========================================
  // BUDGET SERVICES (KES 250 – 1,999)
  // ==========================================
  {
    id: "online-cyber-services",
    tier: "budget",
    name: "Online Cyber Services",
    tagline: "Fast, affordable digital assistance",
    price: "KES 250 – 300",
    priceMin: 250,
    priceMax: 300,
    description: "Quick online assistance including form filling, document processing, printing support, scanning, and basic cyber services.",
    features: [
      "Form filling & submissions",
      "Document printing & scanning",
      "Online applications",
      "Basic IT assistance"
    ],
    target: "Individuals, students, walk-in clients",
    image: "assets/services/online-cyber-services.png",
    whatsapp: "Hi KDCN, I'm interested in Online Cyber Services (KES 250-300). Please share details."
  },
  {
    id: "poster-flyer-design",
    tier: "budget",
    name: "Poster & Flyer Design",
    tagline: "Professional designs that attract attention",
    price: "KES 500 – 699",
    priceMin: 500,
    priceMax: 699,
    description: "Custom-designed posters and flyers for events, businesses, promotions, and personal projects.",
    features: [
      "Custom design",
      "Print-ready files",
      "2 revisions included",
      "Fast turnaround (24-48 hours)"
    ],
    target: "Event organizers, businesses, individuals",
    image: "assets/services/poster-flyer-design.jpg",
    whatsapp: "Hi KDCN, I'd like a Poster & Flyer Design quote (KES 500-699). Here's my project: "
  },
  {
    id: "business-email-setup",
    tier: "budget",
    name: "Business Email Setup",
    tagline: "Look professional with branded email",
    price: "KES 1,000 – 1,249",
    priceMin: 1000,
    priceMax: 1249,
    description: "Professional business email setup on your domain. Includes configuration, testing, and delivery verification.",
    features: [
      "Custom domain email (you@yourdomain.com)",
      "Full configuration",
      "Spam protection setup",
      "Mobile + desktop setup guidance"
    ],
    target: "Businesses with a domain name",
    image: "assets/services/business-email-setup.png",
    whatsapp: "Hi KDCN, I need Business Email Setup (KES 1,000-1,249). My domain is: "
  },

  // ==========================================
  // MID-TIER SERVICES (KES 1,500 – 7,299)
  // ==========================================
  {
    id: "cv-cover-letter",
    tier: "mid",
    name: "CV & Cover Letter Package",
    tagline: "Stand out in the job market",
    price: "KES 1,500 – 1,699",
    priceMin: 1500,
    priceMax: 1699,
    description: "Professional CV and cover letter writing/redesign tailored to your target role and industry.",
    features: [
      "ATS-friendly CV",
      "Custom cover letter",
      "LinkedIn profile tips",
      "PDF + Word formats"
    ],
    target: "Job seekers, professionals, graduates",
    image: "assets/services/cv-cover-letter.png",
    whatsapp: "Hi KDCN, I want the CV & Cover Letter Package (KES 1,500-1,699). My target role is: "
  },
  {
    id: "google-my-business",
    tier: "mid",
    name: "Google My Business Listing",
    tagline: "Get found on Google Maps",
    price: "KES 1,500 – 1,849",
    priceMin: 1500,
    priceMax: 1849,
    description: "Complete setup and optimization of your Google Business Profile for local visibility.",
    features: [
      "Business profile creation",
      "Category & keyword optimization",
      "Photos & description setup",
      "Verification assistance"
    ],
    target: "Local businesses, shops, service providers",
    image: "assets/services/google-my-business.png",
    whatsapp: "Hi KDCN, I need Google My Business Listing (KES 1,500-1,849). My business: "
  },
  {
    id: "starter-digital-access",
    tier: "mid",
    name: "Starter Digital Access Package",
    tagline: "Everything you need to get online",
    price: "KES 1,500 – 2,000",
    priceMin: 1500,
    priceMax: 2000,
    description: "Complete starter kit for getting your digital presence online — email, basic profile, and setup.",
    features: [
      "Professional email setup",
      "Basic online profile",
      "Digital account setup",
      "1-hour training session"
    ],
    target: "Individuals, students, job seekers",
    image: "assets/services/starter-digital-access.png",
    whatsapp: "Hi KDCN, I'm interested in the Starter Digital Access Package (KES 1,500-2,000)."
  },
  {
    id: "digital-strategy-consultation",
    tier: "mid",
    name: "Digital Strategy Consultation",
    tagline: "Get a clear online direction",
    price: "KES 1,500 – 2,999",
    priceMin: 1500,
    priceMax: 2999,
    description: "One-on-one consultation to define your digital strategy, roadmap, and next steps.",
    features: [
      "60-minute session",
      "Custom digital roadmap",
      "Tool recommendations",
      "Follow-up summary document"
    ],
    target: "Entrepreneurs, business owners",
    image: "assets/services/digital-strategy-consultation.png",
    whatsapp: "Hi KDCN, I'd like a Digital Strategy Consultation (KES 1,500-2,999). My business: "
  },
  {
    id: "professional-career",
    tier: "mid",
    name: "Professional Career Package",
    tagline: "Complete career launch kit",
    price: "KES 3,000 – 3,500",
    priceMin: 3000,
    priceMax: 3500,
    description: "Full career package — CV, cover letter, LinkedIn optimization, and interview preparation.",
    features: [
      "Professional CV",
      "Custom cover letter",
      "LinkedIn profile optimization",
      "Interview prep guide"
    ],
    target: "Job seekers, professionals",
    image: "assets/services/professional-career.png",
    whatsapp: "Hi KDCN, I want the Professional Career Package (KES 3,000-3,500)."
  },
  {
    id: "logo-branding",
    tier: "mid",
    name: "Logo & Branding Package",
    tagline: "Create a memorable brand identity",
    price: "KES 3,000 – 4,199",
    priceMin: 3000,
    priceMax: 4199,
    description: "Complete brand identity package with logo design, color palette, and brand guidelines.",
    features: [
      "3 logo concepts",
      "Final logo in all formats",
      "Brand color palette",
      "Basic brand guidelines"
    ],
    target: "Startups, SMEs, rebranding businesses",
    image: "assets/services/logo-branding.jpg",
    whatsapp: "Hi KDCN, I need Logo & Branding Package (KES 3,000-4,199). My business: "
  },
  {
    id: "business-startup",
    tier: "mid",
    name: "Business Startup Package",
    tagline: "Launch your business properly",
    price: "KES 5,000 – 6,000",
    priceMin: 5000,
    priceMax: 6000,
    description: "Complete startup kit including brand identity, basic website, and digital setup.",
    features: [
      "Logo & brand basics",
      "Basic website (3 pages)",
      "Business email",
      "Social media setup"
    ],
    target: "SMEs, startups, entrepreneurs",
    image: "assets/services/business-startup.png",
    whatsapp: "Hi KDCN, I want the Business Startup Package (KES 5,000-6,000)."
  },
  {
    id: "social-media-management",
    tier: "mid",
    name: "Social Media Management",
    tagline: "Grow your online presence",
    price: "KES 5,000 – 7,299",
    priceMin: 5000,
    priceMax: 7299,
    description: "Monthly social media management for 2-3 platforms including content creation and posting.",
    features: [
      "Content calendar",
      "12-15 posts per month",
      "2-3 platforms",
      "Engagement & reporting"
    ],
    target: "Businesses, influencers, brands",
    image: "assets/services/social-media-management.jpg",
    whatsapp: "Hi KDCN, I'm interested in Social Media Management (KES 5,000-7,299/month)."
  },

  // ==========================================
  // ENTERPRISE SERVICES (KES 10,999 – 40,000)
  // ==========================================
  {
    id: "website-promo",
    tier: "enterprise",
    name: "Website Promo Package",
    tagline: "Limited offer — professional website",
    price: "KES 10,999 – 22,000",
    priceMin: 10999,
    priceMax: 22000,
    description: "Limited-time offer on a professional business website. Includes design, development, and launch.",
    features: [
      "5-7 page custom website",
      "Mobile responsive",
      "Basic SEO setup",
      "1-month support"
    ],
    target: "Growing businesses",
    image: "assets/services/website-promo.png",
    badge: "LIMITED OFFER",
    whatsapp: "Hi KDCN, I'm interested in the Website Promo Package (KES 10,999-22,000)."
  },
  {
    id: "cross-platform-growth",
    tier: "enterprise",
    name: "Cross-Platform Growth Bundle",
    tagline: "Grow your brand everywhere",
    price: "KES 12,000 – 15,000",
    priceMin: 12000,
    priceMax: 15000,
    description: "Complete social media growth bundle across Instagram, Facebook, TikTok, YouTube, and X (Twitter).",
    features: [
      "5 platforms setup & optimization",
      "Brand templates",
      "Content strategy",
      "Monthly analytics report"
    ],
    target: "Businesses expanding online",
    image: "assets/services/cross-platform-growth.png",
    whatsapp: "Hi KDCN, I want the Cross-Platform Growth Bundle (KES 12,000-15,000)."
  },
  {
    id: "website-design",
    tier: "enterprise",
    name: "Website Design Package",
    tagline: "Professional custom website",
    price: "KES 15,000 – 17,499",
    priceMin: 15000,
    priceMax: 17499,
    description: "Full custom website design and development for small businesses, startups, and organizations.",
    features: [
      "7-10 page website",
      "Custom design",
      "Mobile optimized",
      "SEO basics + 3-month support"
    ],
    target: "Small businesses, startups, organizations",
    image: "assets/services/website-design.jpg",
    whatsapp: "Hi KDCN, I need Website Design Package (KES 15,000-17,499)."
  },
  {
    id: "business-digital-presence",
    tier: "enterprise",
    name: "Business Digital Presence Package",
    tagline: "Complete digital foundation",
    price: "KES 20,000 – 25,999",
    priceMin: 20000,
    priceMax: 25999,
    description: "Complete digital foundation for growing businesses — website, brand, social, and email.",
    features: [
      "Custom website",
      "Full brand identity",
      "Business email setup",
      "Social media setup"
    ],
    target: "Growing businesses",
    image: "assets/services/business-digital-presence.png",
    whatsapp: "Hi KDCN, I want the Business Digital Presence Package (KES 20,000-25,999)."
  },
  {
    id: "premium-brand-tech",
    tier: "enterprise",
    name: "Premium Brand & Tech Package",
    tagline: "Enterprise-grade digital setup",
    price: "KES 35,000 – 40,000",
    priceMin: 35000,
    priceMax: 40000,
    description: "Complete enterprise digital package for corporates, NGOs, and serious brands.",
    features: [
      "Premium custom website",
      "Full brand system",
      "Cloud infrastructure setup",
      "Security configuration",
      "6-month support"
    ],
    target: "Corporates, NGOs, serious brands",
    image: "assets/services/premium-brand-tech.png",
    badge: "PREMIUM",
    whatsapp: "Hi KDCN, I'm interested in the Premium Brand & Tech Package (KES 35,000-40,000)."
  }
];

// ==========================================
// HELPERS
// ==========================================
function getServiceById(id) {
  return KDCN_SERVICES.find(s => s.id === id);
}

function getServicesByTier(tier) {
  return KDCN_SERVICES.filter(s => s.tier === tier);
}

function getAllServices() {
  return KDCN_SERVICES;
}

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { KDCN_SERVICES, getServiceById, getServicesByTier, getAllServices };
}
