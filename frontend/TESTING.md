# Frontend Testing Guide

## Manual Testing Checklist

### Basic Functionality
- [ ] Page loads without errors
- [ ] Chess board displays correctly (8x8 grid)
- [ ] All pieces appear in starting positions
- [ ] Board colors alternate correctly

### Game Creation
- [ ] "New Game" button creates a new game
- [ ] Game status shows "Active"
- [ ] Current turn shows "White"
- [ ] Move count shows "0"

### Piece Selection
- [ ] Clicking white piece selects it (green highlight)
- [ ] Selected piece shows pulsing animation
- [ ] Valid move indicators appear (green dots)
- [ ] Clicking black piece when white's turn shows error
- [ ] ESC key clears selection

### Move Execution
- [ ] Valid move executes successfully
- [ ] Board updates with new piece position
- [ ] Turn switches to opponent
- [ ] Move count increments
- [ ] Move appears in history

### Move Validation
- [ ] Cannot move opponent's pieces
- [ ] Cannot move to invalid squares
- [ ] Error message displays for invalid moves
- [ ] Cannot move after game ends

### Visual Feedback
- [ ] Hover effect on current player's pieces
- [ ] Selected piece highlights in green
- [ ] Valid moves show green dots
- [ ] Messages auto-clear after 3 seconds
- [ ] Smooth animations on all interactions

### Keyboard Shortcuts
- [ ] ESC clears selection
- [ ] N prompts for new game
- [ ] Confirmation dialog appears for new game

### Game States
- [ ] Check status displays correctly
- [ ] Checkmate ends game
- [ ] Stalemate ends game
- [ ] Cannot move after game over

### Move History
- [ ] Moves appear in history panel
- [ ] History shows piece type and positions
- [ ] Captured pieces noted in history
- [ ] History scrolls for long games

### Responsive Design
- [ ] Layout works on desktop
- [ ] Layout works on tablet (if available)
- [ ] Layout works on mobile (if available)

### Error Handling
- [ ] Backend offline shows error message
- [ ] Invalid API responses handled gracefully
- [ ] Network errors display user-friendly messages

## Browser Testing

Test in multiple browsers:
- [ ] Chrome/Chromium
- [ ] Firefox
- [ ] Safari
- [ ] Edge

## Performance Testing

- [ ] Page loads in < 2 seconds
- [ ] Moves execute in < 500ms
- [ ] No memory leaks after 50+ moves
- [ ] Smooth animations (60fps)

## API Integration Testing

### Test with curl:

```bash
# Create game
curl -X POST http://localhost:5001/api/game/new

# Make move
curl -X POST http://localhost:5001/api/game/game_1/move \
  -H "Content-Type: application/json" \
  -d '{"from": [6, 4], "to": [4, 4]}'

# Get state
curl http://localhost:5001/api/game/game_1/state

# Get history
curl http://localhost:5001/api/game/game_1/history
```

## Common Issues

### Issue: Pieces not moving
**Solution:** Check browser console, verify backend is running

### Issue: CORS errors
**Solution:** Ensure Flask-CORS is installed and backend is on port 5001

### Issue: Moves not validating
**Solution:** Check API responses in Network tab

### Issue: Visual glitches
**Solution:** Clear browser cache, hard refresh (Cmd+Shift+R)

## Automated Testing (Future)

Consider adding:
- Jest for JavaScript unit tests
- Cypress for E2E testing
- Lighthouse for performance audits
