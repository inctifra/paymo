# Event Dashboard Documentation

A modern, professional dashboard for event organizers to manage their events, track analytics, and monitor performance.

## 🎯 Access the Dashboard

**URL**: `http://localhost:8000/dashboard/`

## ✨ Features

### 1. **Sidebar Navigation**
- **Dashboard Overview** - Main analytics view
- **My Events** - List and manage all events (with count badge)
- **Tickets** - Ticket management
- **Attendees** - Attendee list and management
- **Reports** - Detailed analytics reports
- **Sales Analytics** - Sales performance tracking
- **Revenue** - Revenue breakdown
- **Settings** - Account and preferences
- **Support** - Help and documentation

### 2. **Top Header**
- **Search Bar** - Quick search for events and attendees
- **Notifications** - Real-time alerts (with badge indicator)
- **User Avatar** - Profile access

### 3. **Stats Overview Cards**
Four key metric cards with real-time data:
- **Total Revenue**: $48,924 (+12.5% vs last month)
- **Tickets Sold**: 2,847 (+8.2% vs last month)
- **Total Attendees**: 3,256 (+15.3% vs last month)
- **Active Events**: 12 events (3 ending this week)

Each card shows:
- Current value with large, bold numbers
- Trend indicator (up/down arrow with percentage)
- Comparison with previous period
- Color-coded gradient top border

### 4. **Revenue Overview Chart**
- **Type**: Line chart with area fill
- **Data**: Last 7 days revenue tracking
- **Features**:
  - Current week vs previous week comparison
  - Smooth curve interpolation
  - Interactive tooltips
  - Time period selector (7/30/90 days)
  - Dollar-formatted Y-axis

### 5. **Ticket Sales Distribution Chart**
- **Type**: Doughnut chart
- **Categories**:
  - VIP: 420 tickets (blue)
  - Regular: 1,250 tickets (orange)
  - Early Bird: 850 tickets (pink)
  - Group: 327 tickets (green)
- **Features**:
  - Percentage breakdown
  - Interactive hover effects
  - Legend at bottom

### 6. **Recent Events Table**
Displays event information with:
- **Event Details**: Thumbnail image, name, location
- **Date**: Event date
- **Tickets Sold**: Progress (sold/capacity)
- **Revenue**: Total earnings
- **Status Badge**: Active/Upcoming/Ended
- **Action Buttons**: View, Edit, Analytics

Current events shown:
1. Summer Music Festival 2026 - 852/1000 tickets - $15,240
2. Live Jazz Night - 245/500 tickets - $8,925
3. Rock Legends Tour - 1,250/1,500 tickets - $24,750

### 7. **Quick Actions**
Three prominent action cards:
- **Create Event** - Start a new event (blue)
- **Promote Event** - Boost visibility (orange)
- **View Reports** - Detailed analytics (pink)

## 🎨 Design Elements

### Color Palette
- **Primary Blue**: #318CE7 (Trust, professionalism)
- **Accent Orange**: #FF8200 (Action, energy)
- **Accent Pink**: #FF0080 (Highlights)
- **Success Green**: #10b981 (Positive metrics)
- **Dark Background**: #1a1a1a (Sidebar)

### Typography
- **Headers**: Urbanist (Bold, modern, impactful)
- **Body**: Lato (Clean, professional, readable)

### Interactive Elements
- **Hover Effects**: All cards and buttons have smooth transitions
- **Gradient Borders**: Top borders on stat cards
- **Animated Charts**: Smooth loading animations
- **Status Badges**: Color-coded for quick recognition
- **Action Buttons**: Icon-based with hover states

## 📊 Chart Implementation

### Technologies Used
- **Chart.js v4.4.0** - For all data visualizations
- **Line Chart**: Revenue tracking with dual datasets
- **Doughnut Chart**: Ticket distribution analysis

### Chart Configuration
- Responsive design (adapts to container size)
- Custom tooltips with dollar formatting
- Smooth animations on load
- Interactive legends
- Grid lines for better readability

## 📱 Responsive Design

### Breakpoints
- **Desktop** (>992px): Full sidebar visible
- **Tablet** (768px-992px): Collapsible sidebar
- **Mobile** (<768px): 
  - Hidden sidebar
  - Simplified header
  - Stacked stat cards
  - Reduced chart heights

## 🔧 Customization

### Update Stats
Edit the values in the stats cards section:
```html
<h2 class="stat-value">$48,924</h2>
<p class="stat-footer">vs. last month $43,500</p>
```

### Add/Remove Navigation Items
Edit the sidebar navigation:
```html
<li>
    <a href="#">
        <i class="bi bi-[icon-name]"></i>
        <span>Menu Item</span>
    </a>
</li>
```

### Modify Chart Data
Update the JavaScript at the bottom:
```javascript
data: {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [{
        data: [4200, 5800, 4500, 7200, 6800, 8400, 9200]
    }]
}
```

### Change Color Scheme
Edit CSS variables at the top:
```css
:root {
    --primary-blue: #318CE7;
    --accent-orange: #FF8200;
    --accent-pink: #FF0080;
}
```

## 🎯 Key Interactions

1. **Stat Cards**: Hover to lift and enhance shadow
2. **Charts**: Hover over data points for detailed tooltips
3. **Table Rows**: Hover to highlight and slightly scale
4. **Action Buttons**: Hover changes color to primary blue
5. **Quick Actions**: Lift effect with shadow on hover
6. **Navigation**: Active state with left border accent

## 📈 Data Flow

### Mock Data Sources
Currently using static mock data for demonstration:
- Revenue: Last 7 days showing $48,924 total
- Tickets: 2,847 sold across all events
- Events: 12 active events with varying completion rates

### Integration Ready
The dashboard is structured to easily integrate with:
- Django backend API endpoints
- Real-time WebSocket updates
- Database queries for live data
- Authentication and permissions

## 🚀 Next Steps for Production

1. **Connect to Backend**
   - Replace mock data with API calls
   - Implement data fetching with AJAX/Axios
   - Add real-time updates with WebSockets

2. **Add Filtering**
   - Date range selectors
   - Event category filters
   - Status filters (Active/Upcoming/Ended)

3. **Implement CRUD Operations**
   - Create new events modal
   - Edit event inline forms
   - Delete confirmations
   - Bulk actions

4. **Export Functionality**
   - PDF reports
   - CSV data exports
   - Chart image downloads

5. **User Permissions**
   - Role-based access control
   - Event owner verification
   - Multi-user collaboration

## 💡 Best Practices

- All styles are embedded for easy deployment
- Charts are fully responsive
- Accessible color contrasts (WCAG AA compliant)
- Semantic HTML structure
- Modern CSS Grid and Flexbox layouts
- Performance optimized (lightweight libraries)

---

**Built with**: Bootstrap 5, Chart.js, Bootstrap Icons, Google Fonts
