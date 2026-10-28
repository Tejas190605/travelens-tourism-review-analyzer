import React, { useState } from 'react';

// Reliable category-tailored high-resolution fallback images
const CATEGORY_FALLBACKS = {
  Heritage: 'https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80',
  Nature: 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=80',
  Coastal: 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80',
  Urban: 'https://images.unsplash.com/photo-1477959858617-67f30bc75b82?auto=format&fit=crop&w=1200&q=80',
  Island: 'https://images.unsplash.com/photo-1542259009477-d625272157b7?auto=format&fit=crop&w=1200&q=80',
  Cultural: 'https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80',
  Default: 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80',
};

export default function DestinationImage({
  src,
  alt = 'Destination',
  className = '',
  category = 'Default',
  style = {},
  loading = 'lazy',
}) {
  const [hasError, setHasError] = useState(false);
  const [isLoaded, setIsLoaded] = useState(false);

  const fallbackSrc = CATEGORY_FALLBACKS[category] || CATEGORY_FALLBACKS.Default;
  const imageSrc = hasError || !src ? fallbackSrc : src;

  return (
    <div
      className={`destination-img-container ${className}`}
      style={{
        position: 'relative',
        overflow: 'hidden',
        backgroundColor: '#e2e8f0',
        ...style,
      }}
    >
      <img
        src={imageSrc}
        alt={alt}
        loading={loading}
        onLoad={() => setIsLoaded(true)}
        onError={() => setHasError(true)}
        style={{
          width: '100%',
          height: '100%',
          objectFit: 'cover',
          display: 'block',
          transition: 'opacity 0.3s ease, transform 0.5s ease',
          opacity: isLoaded ? 1 : 0.7,
        }}
      />
    </div>
  );
}
