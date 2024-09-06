document.addEventListener('DOMContentLoaded', () => {
    const showMoreBtn = document.getElementById('showMoreBtn');
    const cards = document.querySelectorAll('.card');
    let visibleCardsCount = 4;

    showMoreBtn.addEventListener('click', () => {
        // Show 4 more cards or all remaining if fewer than 4
        for (let i = visibleCardsCount; i < visibleCardsCount + 4 && i < cards.length; i++) {
            cards[i].style.display = 'block';
        }

        // Update the number of visible cards
        visibleCardsCount += 4;

        // Hide the Show More button if no more cards to show
        if (visibleCardsCount >= cards.length) {
            showMoreBtn.style.display = 'none';
        }
    });
});

// artist button
document.addEventListener('DOMContentLoaded', () => {
    const showMoreBtn = document.getElementById('showMoreBtn1');
    const hiddenCards = document.querySelectorAll('.card.hidden');
    let visibleCardsCount = 4;

    showMoreBtn.addEventListener('click', () => {
        // Show 4 more cards or all remaining if fewer than 4
        for (let i = visibleCardsCount; i < visibleCardsCount + 4 && i < hiddenCards.length; i++) {
            hiddenCards[i].style.display = 'block';
        }

        // Update the number of visible cards
        visibleCardsCount += 4;

        // Hide the Show More button if no more cards to show
        if (visibleCardsCount >= hiddenCards.length) {
            showMoreBtn.style.display = 'none';
        }
    });
});